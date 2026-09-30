from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime 

from create_table import create_table
from load_data import load_data
from analyze_data import analyze_data
from plot_data import plot_data

with DAG(
    dag_id="bio_etl_dag",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    task_create_table = PythonOperator(
        task_id="create_table",
        python_callable=create_table
    )

    task_load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    task_analyze_data = PythonOperator(
        task_id="analyze_data",
        python_callable=analyze_data
    )

    task_plot_data = PythonOperator(
        task_id="plot_data",
        python_callable=plot_data
    )

    task_create_table >> task_load_data >> task_analyze_data >> task_plot_data