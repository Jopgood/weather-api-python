"""Basic connection example.
"""

import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.environ['REDIS_CONNECTION_STRING'],
    port=17126,
    decode_responses=True,
    username="default",
    password=os.environ['REDIS_PASSWORD'],
)

