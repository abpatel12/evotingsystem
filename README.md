# Electronic Voting System (Educational Prototype)

A local Flask + MySQL prototype aligned with the group's Part One and Part Two requirements. It is for coursework demonstration with synthetic/test data only, **not for real elections**.

## Implemented in this starter project
- Voter/admin login with password hashing (Werkzeug) and optional TOTP MFA support.
- Role-based access control enforced on the server.
- Login throttling (simple in-process demonstration; use a shared store for multi-worker deployment).
- Eligibility checks and cryptographically random, one-time, expiring voting tokens.
- Atomic token consumption and ballot insertion using a MySQL transaction.
- Separation of voter/token state from anonymous ballot records.
- HMAC integrity tags for ballots and result snapshots.
- Independent recount function and publication gate.
- Security audit events, health endpoint, backup helper, and unit tests.

## Important limitations
This is a **teaching prototype**, not a production election system. It does not provide end-to-end verifiability, coercion resistance, a formal cryptographic anonymity guarantee, tamper-proof external logging, hardened key management, production-grade rate limiting, or high availability. TOTP MFA is optional per user in the seed data. Do not use real voter information or real elections.

## Requirements
- Python 3.10+
- MySQL Server 8+
- VS Code (recommended)

## 1. Create database
In MySQL Workbench, run `sql/schema.sql`. It creates the database and tables.

## 2. Configure environment
Copy `.env.example` to `.env` and update `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, and `MYSQL_PASSWORD`.
Set a long random `APP_SECRET_KEY` and `VOTE_HMAC_KEY` (both should be kept private). Example values are placeholders only.

Generate keys using Python:
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```
Run it twice and use different values for the two keys.

## 3. Create and activate virtual environment (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If `py` is unavailable, try `python` instead. If PowerShell blocks activation, use `.\.venv\Scripts\activate.bat` from Command Prompt.

## 4. Start the app
```powershell
python run.py
```
Open `http://127.0.0.1:5000`.

## 5. Seed demo data
After configuring `.env`, run:
```powershell
python seed_demo.py
```
This creates demo accounts and a sample election/candidates. **Change demo passwords before any shared demonstration.** The seed command refuses to run if the database has existing users.

Demo credentials created by the seed script:
- Voter: `voter1` / `ChangeMe-Voter-2026!`
- Admin: `admin1` / `ChangeMe-Admin-2026!`

If TOTP is enabled in the seed script, the setup secret is printed in the terminal. The default seed sets TOTP disabled so you can first test the workflow. Enable TOTP in MySQL for a user and enrol an authenticator app before relying on MFA.

## Tests
Unit tests use mocks and do not require a live MySQL server:
```powershell
python -m unittest discover -s tests -v
```

## API endpoints
- `POST /api/login`
- `POST /api/logout`
- `GET /api/elections`
- `POST /api/voting/token`
- `POST /api/votes`
- `POST /api/admin/count`
- `POST /api/admin/verify-results`
- `GET /api/admin/audit-logs`
- `GET /api/health`

## Security notes
- Production deployments must use HTTPS, secure cookie settings, a CSRF defence, a shared rate-limit store, externalised secrets, independent security review, and a tested recovery plan.
- The ballot table intentionally contains no user ID or voting-token ID. Application logs must not record candidate selections.


## Repository layout

- `evoting/`: application package facade.
- `app/`: Flask routes, database integration, templates, static assets, and core security implementation.
- `scripts/`: helper scripts for demo seeding and database backups.
- `tests/`: automated tests.
- Root helper modules (`audit_logger.py`, `rate_limiter.py`, `rbac.py`, `result_integrity.py`, `service_monitor.py`, `vote_token.py`) expose reusable functions.
- `.env.example`: configuration template. Copy it to `.env` and replace every placeholder locally. Real `.env` files and credentials are intentionally not included in this archive.

Install dependencies with `pip install -r requirements.txt`, configure `.env`, initialise the MySQL schema from `sql/schema.sql`, and run `python run.py`. This is an educational prototype, not a system for real elections.
