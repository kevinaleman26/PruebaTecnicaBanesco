from dataclasses import dataclass

@dataclass
class Geo:
    lat: str = ""
    lon: str = ""

    def __init__(self, dt):
        self.lat = dt['lat']
        self.lon = dt['lng']

    def __repr__(self):
        return f"Geo(Latitud='{self.lat}', Longitud='{self.lon}')"