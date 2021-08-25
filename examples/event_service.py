from typing import Dict, List
import requests


DEFAULT_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
)


class EventService:
    url: str

    def __init__(self, url=DEFAULT_URL):
        self.url = url

    def get_events(self) -> List[Dict]:
        response = requests.get(self.url)
        response.raise_for_status()
        geojson = response.json()
        return geojson["features"]
