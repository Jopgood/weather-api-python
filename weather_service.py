from typing import Dict, Optional
import httpx
from redis_client import redis_client

class WeatherService:
    def __init__(self):
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services"  # Api Services root
        self.cache_ttl = 1800  # 30 minutes cache

    async def get_weather(self, city: str, clear_cache=False) -> Dict:
        # Try to get from cache first
        cache_key = f"weather:{city}"

        if clear_cache:
            await redis_client.delete(cache_key)
     
        cached_data = await redis_client.get(cache_key)
        
        if cached_data:
            return [cached_data, 'from cache']

        # If not in cache, fetch from external API
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/timeline/{city}",
                    params={
                        "key": "EAUAFFRDNRP23RE6KKSWAXXPK",  # TODO: Create a config file for this
                        "unitGroup": 'metric',
                        "include": 'current',
                        "contentType": 'json'
                    }
                )
                response.raise_for_status()
                weather_data = response.json()

                # Cache the response
                await redis_client.set(
                    cache_key,
                    weather_data,
                    expire=self.cache_ttl
                )

                return weather_data
            except httpx.HTTPError as e:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Weather API error: {str(e)}"
                )