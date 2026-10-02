# Expected Demo Findings

The exact set depends on the versions of CodeQL, Joern/LLM analysis, Snyk,
your correlation rules, and your configured security/licence policies.

## Source code
- SQL Injection candidate in `src/app.py`
- Path Traversal candidate in `src/app.py`
- Reflected HTML/XSS-style output in `src/app.py`
- Weak MD5 hashing in `src/app.py`
- Hard-coded dummy secret in `src/app.py`

## Dependencies
`requirements.txt` contains intentionally old packages to exercise SCA.
Exact CVEs returned are database-dependent.

## Container
`Dockerfile` / `docker-compose.yml` contain demo-only weak settings such as:
- old base image
- root execution
- dummy secrets in environment variables

## Infrastructure
Terraform and Kubernetes manifests intentionally contain:
- SSH open to `0.0.0.0/0`
- public S3 access settings
- privileged Kubernetes container
- root user configuration

## Licence
`PyMuPDF==1.23.3` is included as a licence-policy test candidate.
Whether FIXORA/Snyk reports it depends on the configured licence policy.

## Best end-to-end defense example
Use the SQL Injection finding:
Detect -> Inspect -> Validate -> Confirm -> Correct -> Review -> Accept/Reject
