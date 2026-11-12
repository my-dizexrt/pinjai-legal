# pinjai-legal

Public pages for the Pinjai (พินใจ) app (`com.pinjai.app`), served with GitHub Pages.

| Page | Path |
|---|---|
| Privacy policy (English) | `/privacy/en/` |
| Privacy policy (Thai) | `/privacy/th/` |
| Account deletion request | `/delete-account/` |

No placeholders left. Contact email: `support@pinjai.com` (forwards to the owner's inbox).
This is a draft prepared for review, not legal advice.

## Security

CI runs gitleaks on the full git history and fails the pull request if a secret is found. Run the same scan locally with `bash scripts/run-gitleaks.sh` (downloads pinned gitleaks v8.30.1, verifies the official checksums file, then scans every ref). This repo has no npm dependencies; Dependabot is configured in `.github/dependabot.yml` for GitHub Actions only (weekly).

The owner enables Dependabot alerts, Dependabot security updates, secret scanning, and push protection under Settings → Security and quality → Advanced Security.
