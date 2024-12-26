from airlfow.decorators import dag,task
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2021,1,1),
    tags=['aws']
)

def my_dag():
    wait_for_file = S3KeySensor(
        task_id = "wait_for_file",
        aws_conn_id = "aws_s3",
        bucket_key="my_bucket/my_key",
        wildcard_match=True
    )

    @task
    def process_file():
        print("File found. Processing file.")

    wait_for_file >> process_file()

my_dag()