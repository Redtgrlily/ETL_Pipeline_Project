from airflow import DAG
from airflow.operations.python_operator import PythonOperator
from scripts.extract import fetch_data
from scripts.transform import transform_data
from scripts.load import load_data
from datetime import datetime

def run_etl():
    df = fetch_data()
    df = transform_data(df)
    load_data(df)
    
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 31),
    'retries': 1,
}

dag = DAG('covid_etl_dag', default_args=default_args, schedule_interval='@daily')

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)