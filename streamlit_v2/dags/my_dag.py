# my_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

from script1 import function_from_script1
from script2 import function_from_script2

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_sample_dag',
    default_args=default_args,
    description='Un DAG simple avec Streamlit',
    schedule_interval='*/5 * * * *',  # Exécuté toutes les 5 minutes
)

t1 = PythonOperator(
    task_id='task_from_script1',
    python_callable=function_from_script1,
    dag=dag,
)

t2 = PythonOperator(
    task_id='task_from_script2',
    python_callable=function_from_script2,
    dag=dag,
)

t3 = BashOperator(
    task_id='start_streamlit_app',
    bash_command='bash run_streamlit.sh', 
    dag=dag,
)

t1 >> t2 >> t3
