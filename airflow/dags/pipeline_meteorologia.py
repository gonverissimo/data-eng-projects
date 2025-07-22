from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import requests

default_args = {
    'owner': 'goncalo',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

def extrair_dados():
    url = "https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.13&hourly=temperature_2m"
    response = requests.get(url)
    dados = response.json()
    df = pd.DataFrame(dados['hourly'])
    df.to_csv('/opt/airflow/dags/meteorologia.csv', index=False)

def transformar_dados():
    df = pd.read_csv('/opt/airflow/dags/meteorologia.csv')
    df['temperature_celsius'] = df['temperature_2m']
    df_filtrado = df[df['temperature_celsius'] > 15]
    df_filtrado.to_csv('/opt/airflow/dags/temperaturas_filtradas.csv', index=False)

with DAG('etl_meteorologia',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    tarefa1 = PythonOperator(
        task_id='extrair_dados',
        python_callable=extrair_dados
    )

    tarefa2 = PythonOperator(
        task_id='transformar_dados',
        python_callable=transformar_dados
    )

    tarefa1 >> tarefa2
