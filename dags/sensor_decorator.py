from airflow.decorators import dag, task
from datetime import datetime
import requests

from airflow.sensors.base import PokeReturnValue

@dag(start_date = datetime(2021,1,1), schedule_interval = '@daily', catchup = False)
def sensor_decorator():
    @task.sensor(poke_interval=30, timeout=3600, mode='poke')
    def check_shibe_availability() -> PokeReturnValue:
        response = requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')
        print(r.status_code)

        if r.status_code == 200:
            condition_met = True
            operator_return_value = r.json()
        else:
            condition_met = False
            operator_return_value = None
            print(f"Shibe URL returned the status code {r.status_code}")

        return PokeReturnValue(is_done=condition_met, xcom_value=operator_return_value)

    # print the URL to the picture
    @task
    def print_shibe_picture_url(url):
        print(url)

    print_shibe_picture_url(check_shibe_availability())


sensor_decorator()