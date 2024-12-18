from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('x_com_dag', start_date = datetime(2022, 1, 1), schedule_inverval = '@daily', catchup = False) as dag:
    
    @task
    def peter_task(ti=None):
        ti.xcom_push(key = 'peter_task', value = 'iphone')
    
    @task
    def lorie_task(ti=None):
        ti.xcom_push(key = 'lorie_task', value = 'samsung')

    @task
    def bryan_task(ti=None):
        phone = ti.xcom_pull(task_ids = ['peter_task', 'lorie_task'], key = 'mobile_phone')
        print(phone)

    peter_task >> lorie_task >> bryan_task