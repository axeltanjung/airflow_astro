from airflow import DAG
from airflow.sensor.python import PythonSensor

def _condition():
    return False

with DAG(
    dag_id = 'sensor_dag',
    start_date = datetime(2021,1,1),
    schedule_interval = '@daily',
    cathcup = False
):
    waiting_for_condition = PythonSensor(
        task_id = 'waiting_for_condition',
        python_callable = _condition,
        poke_interval = 60,
        timeout= 7*24*60*60
    )

