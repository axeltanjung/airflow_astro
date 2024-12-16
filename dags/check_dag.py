from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

with DAG('check_dag', start_date=datetime(2023, 1, 1),
         description='DAG to check data', tags=['data-engineering'], catchup=False,
         schedule_interval='0 0 * * *') as dag:

    create_file = BashOperator(task_id='create_file', bash_command='echo "Hi, this is a test file" > /tmp/dummy')
    check_file = BashOperator(task_id='check_file', bash_command='test -f /tmp/dummy')
    read_file = PythonOperator(task_id='read_file', python_callable=lambda: print(open('/tmp/dummy', 'rb').read()))

    create_file >> check_file >> read_file