from airflow.decarators import DAG, task
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime

@dag(start_date = datetime(2022, 1, 2), schedule_interval = 'None', catchup = False)
def fetch_cookies_data():

    @task
    def fetch_data_from_snowflake():
        # Connect to snowflake
        conn = SnowflakeHook(snowflake_conn_id = 'snowflake_de').get_conn()
        cursor = conn.cursor()

        # Fetch data from the "cookies" table in the "public" schema
        cursor.execute('SELECT * FROM public.cookies')
        data = cursor.fetchall()
        print(data)

        # Close the connection
        cursor.close()
        conn.close()

        return data

    @task
    def transform_data(data):
        return data
    
    @task
    def store(data):
        print(data)

    store(transform_data(fetch_data_from_snowflake()))

dag = fetch_cookies_data()