# ETL Airflow Project - Local Weather

## This project simulates a more "professional" data pipeline using Apache Airflow with scheduling and monitoring.

It uses historical meteorological data fetched from a public API: https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.13&hourly=temperature_2m

The pipeline consists of a DAG that performs the following tasks:
- Extracts meteorological data from the API and saves it as a CSV file.
- Transforms the data by filtering temperatures above 15°C, creating a new CSV file.
- Allows monitoring task status (success or failure) via the Airflow UI.

The project runs locally using Docker to manage services (Airflow, PostgreSQL, Redis).
A .env file is used to handle environment-specific settings. In particular: AIRFLOW_UID=50000
At the end of the pipeline execution, the CSV files with the extracted and transformed data are available in the `dags/` folder.

Technologies used: Apache Airflow, Python, Docker, Pandas.
