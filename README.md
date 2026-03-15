# Medicine Marketplace MVP

## 🚀 Overview
This repository is a minimal (MVP) implementation of a medicine marketplace backend and frontend.

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React + Vite

---

## ✅ Prerequisites

### Required tools
- Docker & Docker Compose (for running the full stack via containers)
- Node.js 18+ (for frontend dev)
- Python 3.10+ (for backend dev)

### (Optional) Recommended local setup
- `pyenv` / `venv` for Python virtual environments
- `npm` or `pnpm` for frontend package management

---

## 🧱 Backend (FastAPI)

### 1) Configuration
Create a `.env` file in the `backend/` folder with the following values:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/medicines
SECRET_KEY=replace_me_with_a_secure_random_string
```

> ⚠️ `SECRET_KEY` must be set before running the backend (used for JWT signing).

### 2) Run via Docker Compose (recommended)

From the repo root:

```bash
docker compose up --build
```

This starts:
- Backend: http://localhost:8000
- PostgreSQL: exposed at localhost:5432

> ✅ **Important:** The backend container does not include migration scripts by default, so you must run migrations from the host (see below).

#### Run database migrations (when using Docker Compose)

While `docker compose` is running, there are two reliable ways to run migrations:

1) **From the host (requires Alembic installed in the current Python environment)**

```bash
cd backend
pip install -r requirements.txt
alembic upgrade head
```

If you see errors like `alembic: command not found` or `python: command not found`, make sure you are using a Python environment that has dependencies installed (e.g. activate your venv or use `python3`):

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
```

2) **From inside the running backend container (only if the backend source + migrations are baked in or mounted)**

By default, the backend image built by `docker compose up --build` does **not** include the Alembic config or migration scripts (they live in `backend/` on the host). If you run:

```bash
docker compose exec backend alembic upgrade head
```

you may see:

- `No 'script_location' key found in configuration`
- `ERROR: Unable to locate configuration file` (or similar)

If you want this to work, you need to either:

- Mount the `backend/` directory into the container, or
- Modify the Dockerfile to include the migration files/config and set the correct working directory.

> ✅ For most development workflows, run migrations from the host instead (method #1 above).

If you stop the stack, restart it first (so Postgres is available) before applying migrations:

```bash
docker compose up -d db
# then run migrations using method #1 above
```

> 🧩 **Migration troubleshooting:** If migrations fail with errors about missing constraints/indexes (e.g., `constraint "..." does not exist`), it usually means the DB is in a partially-migrated state. Reset by dropping/recreating the database (or schema) and rerunning:
>
> ```bash
> docker compose exec db psql -U postgres -c "DROP DATABASE IF EXISTS medicines;"
> docker compose exec db psql -U postgres -c "CREATE DATABASE medicines;"
> cd backend
> alembic upgrade head
> ```
>
> ⚠️ **Note:** `DROP DATABASE` cannot run inside a transaction block, so it must be run as a standalone command (as shown above). If you still have trouble, ensure no connections are active on the `medicines` database before dropping it.

#### Alembic quick reference

When working with migrations, these commands are handy:

```bash
# Show current applied revision
alembic current

# Show revision history (latest first)
alembic history --verbose

# Generate a new revision stub (edit it before applying)
alembic revision --autogenerate -m "describe changes"

# Apply all pending migrations
alembic upgrade head

# Roll back one revision (or to a named revision)
alembic downgrade -1
alembic downgrade <revision_id>
```

To stop the stack:

```bash
docker compose down

docker compose down -v (to remove volumes)
```

### 3) Run locally (without Docker)

From the repo root, create and activate a virtual environment (if you don't already have one):

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure the database is running (e.g., via Docker):

```bash
docker compose up -d db
```

Run database migrations (required before starting the backend):

```bash
cd backend
alembic upgrade head
```

Start the backend server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> 🔎 If you add/modify models, create a new migration:
>
> ```bash
> alembic revision --autogenerate -m "describe changes"
> alembic upgrade head
> ```

---

## 🌐 Frontend (React + Vite)

From the repo root:

```bash
cd frontend
npm install
npm run dev
```

Then visit:

- http://localhost:5173

---

## 🧪 API Endpoints (for sanity checks)

### Health

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok"}
```

### Register a new user

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

### Log in (get JWT token)

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

Expected response:

```json
{"access_token":"<JWT_TOKEN>"}
```

### Get current user (authenticated)

```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer <JWT_TOKEN>"
```

### Admin-only endpoint (requires `role = admin` in DB)

```bash
curl http://localhost:8000/auth/admin/test \
  -H "Authorization: Bearer <JWT_TOKEN>"
```

> ⚙️ To make a user an admin (quick dev step):
>
> ```bash
> docker compose exec db psql -U postgres -d medicines -c "UPDATE users SET role='admin' WHERE email='test@example.com';"
> ```

---

## 🗃️ Inspect database (Postgres)

Using the running Postgres container:

```bash
docker compose exec db psql -U postgres -d medicines
```

Then run:

```sql
\dt
SELECT * FROM users LIMIT 5;
```

---

## 🛠️ Notes / Developer Tips

- The backend does **not** auto-create tables at startup; migrations must be applied (`alembic upgrade head`) whenever you start the backend (local or Docker).
- When running via Docker Compose, the backend container does not include the migration files; run migrations from the `backend/` directory on your host machine.
- If you change database models, generate a new migration and apply it.

---

## 📌 Where things live

- Backend: `backend/app/`
- Backend API routers: `backend/app/routers/`
- Frontend: `frontend/src/`
- Database migrations: `backend/alembic/`
- Swagger: http://localhost:8000/docs