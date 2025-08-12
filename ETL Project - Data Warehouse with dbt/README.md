# Data Warehouse with dbt and PostgreSQL (Docker)

This project demonstrates a simple data warehouse pipeline using **dbt** (Data Build Tool) and **PostgreSQL** running in Docker.

The pipeline consists of three layers:  
- **Raw**: loading original CSV data into the `raw` schema.  
- **Staging**: initial transformations for cleaning and organizing data.  
- **Analytics**: aggregations and reports for analysis, e.g. total spending per customer.

---

## Key Features

- PostgreSQL container with separate schemas for raw and analytics data.  
- dbt models organized in `raw`, `staging`, and `analytics` folders.  
- Python script to load CSV data into the `raw` schema.  
- Simple dbt tests and model documentation via `schema.yml`.  
- Automated dbt runs to materialize models.  
- Query final results directly in PostgreSQL.

---

## Technologies Used

- [dbt-core] with [dbt-postgres adapter]
- PostgreSQL 15 running in Docker  
- Python 3.9+ (pandas) for data loading  
- Docker for PostgreSQL container management

---

## Commands

- Start PostgreSQL Docker container:
docker run --name postgres-dbt \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=warehouse \
  -p 5432:5432 \
  -d postgres:15

- Configure dbt profile by creating or editing the file ~/.dbt/profiles.yml with the following content:
dbt_project:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: admin
      password: admin
      port: 5432
      dbname: warehouse
      schema: analytics

- Create the raw schema in PostgreSQL:
docker run --name postgres-dbt -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=warehouse -p 5432:5432 -d postgres:15
docker exec -it postgres-dbt psql -U admin -d warehouse

- At the PostgreSQL prompt, run:
create schema raw;
\dn
\q

- Load CSV data into the raw.vendas table by running the Python script:
python .\load_raw.py

- Run dbt models by navigating to the dbt project directory and executing:
cd dbt_project
dbt run (if it does not run directly here, temporarily add the location of the dbt executable to the path)

- Validate results in PostgreSQL by accessing the container again:
docker exec -it postgres-dbt psql -U admin -d warehouse

- And querying the transformed data:
select * from analytics.stg_vendas;
select * from analytics.vendas_por_cliente;
\q