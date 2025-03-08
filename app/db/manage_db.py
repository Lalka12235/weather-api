from pymongo import MongoClient
from app.data.weather_model import Weather

client = MongoClient('localhost',27017)

weather_db = client.weather

weather_collection = weather_db.weather_col

def get_data_weather(city: str):
    result = weather_collection.find_one({'city':city})
    if result:
        return Weather(**result['weather'])
    else:
        return None

def insert_data_weather(weather: Weather,city):
    exist_data = weather_collection.find_one({'city': city})
    if not exist_data:
        result = weather_collection.insert_one(
            {
                'city': city,
                'weather': weather,
            }
        )
        return result
    else:
        get_data_weather(city)


