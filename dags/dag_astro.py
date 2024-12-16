from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.utils.helpers import chain

def print_a():
    print('This is task A')

def print_b():
    print('This is task B')

def print_c():
    print('This is task C')

def print_d():
    print('This is task D')

def print_e():
    print('This is task E')

default_args = {
    'retries': 3
}

with DAG('dag_astro', start_date=datetime(2021, 1, 1),
         description='A simple tutorial DAG', tags=['data-science'], catchup=False,
         schedule_interval='@daily') as dag:

    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b)
    task_c = PythonOperator(task_id='task_c', python_callable=print_c)
    task_d = PythonOperator(task_id='task_d', python_callable=print_d)
    task_e = PythonOperator(task_id='task_e', python_callable=print_e)

    chain(task_a, [task_b, task_c], [task_d, task_e])