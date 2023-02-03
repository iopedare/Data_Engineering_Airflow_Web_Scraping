from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from fetch.fuel import Fuel
from fetch.weather import Weather

dag = DAG(
    dag_id = 'run_hourly_tasks_dag',
    start_date = datetime(2023, 2, 2),
    schedule_interval = "@hourly"
)

run_fetch_nigerian_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_nigeran_fuel',
    python_callable=Fuel('Nigeria').fetch_fuel
)

run_fetch_kenyan_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_kenyan_fuel',
    python_callable=Fuel('Kenya').fetch_fuel
)

run_fetch_nigerian_weather = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_nigeran_weather',
    python_callable=Weather('lagos').fetch_weather
)

run_fetch_kenyan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_kenyan__weather',
    python_callable=Weather('nairobi').fetch_weather
)