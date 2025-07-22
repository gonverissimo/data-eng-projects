# ETL Project - TMDb Movies

This project implements a complete ETL pipeline that extracts real data from the public TMDb (The Movie Database) API, transforms the data, and loads it into a SQL Server database. It demonstrates how to build an automated data extraction, transformation, and loading workflow using Python with the `requests`, `pandas`, and `sqlalchemy` libraries.

The pipeline consists of the following steps:
- Extracts data from the TMDb API (popular movies endpoint) with pagination support.
- Transforms the data by:
  - Converting to a pandas DataFrame.
  - Parsing `release_date` to datetime format.
  - Dropping records with missing release dates.
  - Filtering and normalizing important columns (`title`, `overview`, etc.).
  - Creating a `release_year` column.
  - Removing duplicate movies by ID.
- Loads the cleaned data into a SQL Server table using `sqlalchemy` with an ODBC connection.

The process is orchestrated by a `main.py` script that runs the ETL pipeline end to end.

Prerequisites:
- Python 3.7+
- `requests` library
- `pandas` library
- `sqlalchemy` library
- ODBC Driver for SQL Server installed
- Accessible SQL Server instance
- A `.env` or `key.env` file containing the `TMDB_API_KEY` environment variable

Project Structure:
- `extract.py` – Extracts movie data from the TMDb API.
- `transform.py` – Cleans and transforms the data.
- `load.py` – Loads the data into a SQL Server table.
- `main.py` – Runs the full ETL pipeline.

Technologies Used: Python, TMDb API, SQL Server, requests, pandas, sqlalchemy.
