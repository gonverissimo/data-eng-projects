# ETL Project - TMDb Movies

## Description
This project implements a complete ETL pipeline that extracts real data from the public TMDb (The Movie Database) API, transforms the data, and loads it into a SQL Server database. The goal is to demonstrate how to build an automated data extraction, transformation, and loading solution using Python with the libraries requests, pandas, and sqlalchemy.

## Prerequisites
- Python 3.7+
- requests library
- pandas library
- sqlalchemy library
- ODBC Driver for SQL Server installed
- SQL Server instance configured and accessible
- `key.env` file with TMDb API key (`TMDB_API_KEY` environment variable)

## Code Explanation

- **extract.py**
  - Extracts data from the TMDb API using the popular movies endpoint.
  - Supports pagination to extract multiple pages of data.

- **transform.py**
  - Converts raw data into a pandas DataFrame.
  - Parses the `release_date` column to datetime format.
  - Filters important columns for analysis.
  - Drops movies without a release date.
  - Cleans and normalizes text fields (`title` and `overview`).
  - Adds a `release_year` column extracted from the release date.
  - Removes duplicate movies by ID.

- **load.py**
  - Creates a connection to the SQL Server using sqlalchemy and ODBC.
  - Loads the DataFrame into a SQL table, replacing existing data.

- **main.py**
  - Orchestrates the ETL process by extracting, transforming, and loading data.