from airflow import DAG
from aiflow.decorators import task
from airflow.providers.snowflake.operator.snowflake import SnowflakeOperator

from datetime import datetime

with DAG ('snowflake_dag', start_date = datetime(2022, 1, 2), schedule_interval = '@daily', catchup = False) as dag:

    execute_request = SnowflakeOperator(
        task_id = 'execute_request',
        snowflake_conn_id = 'snowflake',
        sql = 'SELECT ID, NAME, IS_SUPERHOST from RAW.RAW_HOSTS limit 10'
    )