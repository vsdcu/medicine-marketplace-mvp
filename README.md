# Medicine Marketplace MVP

## Prerequisites
- Docker
- Docker Compose

## Run

docker-compose up --build

Backend:
http://localhost:8000
Health check:
http://localhost:8000/health


Checking database tables
-------------------------
exec the postgres container
# psql -U postgres -h localhost -d medicines
psql (15.16 (Debian 15.16-1.pgdg13+1))
Type "help" for help.

medicines=# \dt
                 List of relations
 Schema |         Name          | Type  |  Owner   
--------+-----------------------+-------+----------
 public | addresses             | table | postgres
 public | alembic_version       | table | postgres
 public | chemist_prices        | table | postgres
 public | chemists              | table | postgres
 public | deliveries            | table | postgres
 public | medicines             | table | postgres
 public | order_items           | table | postgres
 public | orders                | table | postgres
 public | prescription_items    | table | postgres
 public | prescriptions         | table | postgres
 public | substitution_consents | table | postgres
 public | users                 | table | postgres
(12 rows)


Frontend:
http://localhost:5173

Building and running the frontend locally

- cd /Users/vinitsaini/workspace/medicine-marketplace-mvp
- source /Users/vinitsaini/workspace/medicine-marketplace-mvp/venv/bin/activate
- cd frontend
- npm install
- npm run dev