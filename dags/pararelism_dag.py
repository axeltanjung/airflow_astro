from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

@dag(
    schedule=None,
    start_date = datetime(2023,1,1),
    tags=['sensor'],
    catchup=False
)

def first_dag():
    wait_for_file = FileSensor.partial(
        task_id = "wait_for_files",
        fs_conn_id = 'fs_default',
    ).expand(
        filepath = ['data_1.csv', 'data_2.csv', 'data_3.csv'],
    )

    @task
    def process_files():
        print("Files found. Processing files.")

    wait_for_file >> process_files()

first_dag()