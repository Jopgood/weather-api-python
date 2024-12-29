import json
from typing import Optional, Any

class RedisClient:
    def __init__(self):
        # In a real environment, we would use redis.Redis()
        # For this example, we'll use a simple in-memory cache
        self._cache = {}

    async def get(self, key: str) -> Optional[Any]:
        if key in self._cache:
            return json.loads(self._cache[key])
        return None

    async def set(self, key: str, value: Any, expire: int = 3600):
        self._cache[key] = json.dumps(value)

    async def delete(self, key: str):
        if key in self._cache:
            del self._cache[key]

redis_client = RedisClient()