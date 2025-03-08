from fastapi import APIRouter
from app.utils.get_weather import get_weather
from app.db.manage_db import insert_data_weather,get_data_weather

router = APIRouter()

@router.get('/get_weather/{city}')
async def location_weather(city: str):
    get_data = get_data_weather(city)
    if not get_data:
        data = get_weather(city)
        insert_data_weather(data,city)
        return data
    else:
        return get_data