from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

from datetime import datetime

def _ml_task(ml_parameter):
    print(ml_parameter)

with DAG('ml_dag', start_date = datetime(2022,1,1),
         schedule_interval = '@daily', catchup = False) as dag:
    
    ml_task = []
    
    for ml_parameter in Variable.get('ml_model_parameter', deserialize_json = True)['params']:
        PythonOperator(
            task_id = f'ml_task_{ml_parameter}',
            python_callable = _ml_task,
            op_kwargs = {'ml_parameter': ml_parameter}
        )

    report = BashOperator(
        task_id = 'report',
        bash_command = 'echo "report_{{ var.value.ml_report_name }}"'
    )

ml_task >> report
