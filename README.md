# FIXORA Demo Project

> Demo-only intentionally vulnerable project. Do not deploy it or expose it to the Internet.

This folder is designed to exercise the main FIXORA scan surfaces:

- Source code
- Python dependencies
- Docker configuration
- Infrastructure-as-Code
- Licence-policy checks
- Dummy secrets
- Git / CI security gates
- JSON / SARIF reporting

## Recommended demo flow

1. Open this folder in VS Code and start FIXORA.
2. Sign in.
3. Run a full-project scan.
4. Open the SQL Injection finding in `src/app.py`.
5. Show location, CWE/severity/evidence and inline diagnostic.
6. Request risk validation (Hacker -> sandbox -> Judge).
7. Confirm the validated finding.
8. Request a secure correction and show Architect -> Sentinel -> patch preview.
9. Accept or reject the patch.
10. Show learning/skill feedback and ask Mentor one short question.
11. Demonstrate a Git security gate with a HIGH finding present.
12. Show the generated JSON / SARIF report or CI result.

## Running the demo app locally

Use only the runtime requirements file:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-runtime.txt
python init_db.py
python src\app.py
```

The app runs on `http://127.0.0.1:5000`.

### Demo endpoints

- `/user?name=alice` — intentionally vulnerable SQL query
- `/download?file=public.txt` — intentionally vulnerable path handling
- `/hello?name=Hadil` — intentionally unsafe HTML output
- `/hash?value=test` — intentionally weak MD5 hashing

All credentials and secrets in this project are fake demo values.

## SCA note

`requirements.txt` is intentionally a scan fixture, not the runtime installation file.
Exact CVE and licence results depend on the vulnerability database and your Snyk policy at scan time.
