
import requests
import sys

import json
                
city = 'london'

def test_city_weather():
    response = requests.request("GET", f"http://127.0.0.1:8000/weather/{city}")
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

    # Parse the results as JSON
    jsonData = response.json()

    print(jsonData)


    assert 'London' in jsonData['resolvedAddress']

    