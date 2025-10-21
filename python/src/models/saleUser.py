from dataclasses import dataclass
from .user import Usuario
from .saleSummary import SaleSummary
from .weather import Weather

@dataclass
class SalesUsuarios:
    userId: int
    name: str
    username: str
    email: str
    weather: Weather
    sale_summary: SaleSummary

    def __init__(self, usuario, sale_summary ):
        self.userId = usuario.id
        self.name = usuario.name
        self.username = usuario.username
        self.email = usuario.email
        self.weather = Weather(lat=usuario.geo.lat, lon=usuario.geo.lon)
        self.sale_summary = sale_summary
        

    def __repr__(self):
        return f"SalesUsuarios(userId='{self.userId}', name='{self.name}', username='{self.username}', email='{self.email}', weather='{self.weather.__repr__()}', sale_summary='{self.sale_summary.__repr__()}')"