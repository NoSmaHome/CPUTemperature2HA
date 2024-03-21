import subprocess
import requests
import json
import time

def get_cpu_temperature():
    process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    temperature_str = output.decode('utf-8').split('=')[1].split('\'')[0]
    temperature_celsius = float(temperature_str)
    return temperature_celsius

def update_home_assistant_entity(temperature):
    api_url = "http://HOMEASSISTANTIP:8123/api/states/sensor.cpu_temperature"
    headers = {
        "Authorization": "Bearer ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    data = {
        "state": temperature,
        "attributes": {
            "unit_of_measurement": "°C",
            "friendly_name": "CPU Temperature Plex"
        }
    }
    response = requests.post(api_url, headers=headers, json=data)
    print("Entity update response:", response.status_code)
   # print("Response Content:", response.content)

if __name__ == "__main__":
    while True:
        temperature = get_cpu_temperature()
        print("CPU Temperature:", temperature)
        update_home_assistant_entity(temperature)
        time.sleep(60)  # Aktualisiere alle 60 Sekunden





