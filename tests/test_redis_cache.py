
import requests
import sys

import json
                
city = 'london'

def test_redis_cache():
    response = requests.request("GET", f"http://127.0.0.1:8000/weather/{city}", params={'clear_cache': True})
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

    assert 'from cache' not in response.json()


    response_redis = requests.request("GET", f"http://127.0.0.1:8000/weather/{city}")
    if response_redis.status_code!=200:
        print('Unexpected Status code: ', response_redis.status_code)
        sys.exit()

    assert 'from cache' in response_redis.json()



    