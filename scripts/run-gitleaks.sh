#!/usr/bin/env bash
# Download a pinned gitleaks release, verify official checksums, and scan full git history.
# Uses the gitleaks binary (not the GitHub Action), so no license key is required.
set -euo pipefail

GITLEAKS_VERSION="8.30.1"
# SHA-256 of the official gitleaks_8.30.1_checksums.txt from the v8.30.1 GitHub release.
GITLEAKS_CHECKSUMS_SHA256="061476c21adaf5441516f96f185c1a4706a83cd6329b9b38762271b3d4a52fae"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "run-gitleaks.sh must be run from a git checkout" >&2
  exit 1
fi

uname_s="$(uname -s | tr '[:upper:]' '[:lower:]')"
uname_m="$(uname -m)"
case "$uname_s" in
  linux) os="linux" ;;
  darwin) os="darwin" ;;
  *)
    echo "unsupported OS: $uname_s (supported: linux, darwin)" >&2
    exit 1
    ;;
esac
case "$uname_m" in
  x86_64 | amd64) arch="x64" ;;
  aarch64 | arm64) arch="arm64" ;;
  *)
    echo "unsupported architecture: $uname_m (supported: x64, arm64)" >&2
    exit 1
    ;;
esac

asset="gitleaks_${GITLEAKS_VERSION}_${os}_${arch}.tar.gz"
base_url="https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}"

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    shasum -a 256 "$1" | awk '{print $1}'
  fi
}

workdir="$(mktemp -d)"
cleanup() { rm -rf "$workdir"; }
trap cleanup EXIT

curl -fsSL -o "$workdir/checksums.txt" "${base_url}/gitleaks_${GITLEAKS_VERSION}_checksums.txt"
actual_sum="$(sha256_file "$workdir/checksums.txt")"
if [[ "$actual_sum" != "$GITLEAKS_CHECKSUMS_SHA256" ]]; then
  echo "gitleaks checksums file hash mismatch:" >&2
  echo "  expected $GITLEAKS_CHECKSUMS_SHA256" >&2
  echo "  actual   $actual_sum" >&2
  exit 1
fi

expected_asset_sum="$(awk -v f="$asset" '$2 == f {print $1}' "$workdir/checksums.txt")"
if [[ -z "$expected_asset_sum" ]]; then
  echo "no checksum for $asset in official checksums file" >&2
  exit 1
fi

curl -fsSL -o "$workdir/$asset" "${base_url}/${asset}"
actual_asset_sum="$(sha256_file "$workdir/$asset")"
if [[ "$actual_asset_sum" != "$expected_asset_sum" ]]; then
  echo "gitleaks archive hash mismatch for $asset:" >&2
  echo "  expected $expected_asset_sum" >&2
  echo "  actual   $actual_asset_sum" >&2
  exit 1
fi

tar -xzf "$workdir/$asset" -C "$workdir" gitleaks
chmod +x "$workdir/gitleaks"

# --all --full-history: every ref, including merge commits. --redact: never print secret values.
exec "$workdir/gitleaks" detect \
  --source "$ROOT" \
  --log-opts="--all --full-history" \
  --redact \
  --verbose \
  --no-banner
