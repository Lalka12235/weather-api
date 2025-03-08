from pydantic import BaseModel

class Weather(BaseModel):
    name: str
    temp: str
    humidity: str
    weather: str
    wind: str