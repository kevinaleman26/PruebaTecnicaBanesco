from dataclasses import dataclass
from .geo import Geo

@dataclass
class Usuario:
    id: str 
    name: str 
    username: str
    email: str 
    geo: Geo 

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.username = data['username']
        self.email = data['email']
        self.geo = Geo(data['address']['geo'])

    def __repr__(self):
        return f"Usuario(Id='{self.id}', Name='{self.name}', Username='{self.username}', Email='{self.email}', Geo='{self.geo.__repr__()}')"