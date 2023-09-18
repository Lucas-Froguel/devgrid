import time
import requests

from devgrid_api.settings import MONGODB_NAME, MONGO_CITIES_DATA_COLLECTION, \
    OPEN_WEATHER_KEY, OPEN_WEATHER_URL
from devgrid_api.mongodb.queries.cities import get_latest_sixty_unchecked_cities
from devgrid_api.mongodb.mongodb import MongoConnection


def scan_db_and_get_cites_data():
    t1 = time.time()
    cities = get_latest_sixty_unchecked_cities()
    if not cities:
        return None

    with MongoConnection() as mongo:
        col = mongo.get_db_collection(MONGODB_NAME, MONGO_CITIES_DATA_COLLECTION)
        for city in cities[0]["city_ids"]:
            data = requests.get(
                OPEN_WEATHER_URL + f"?id={city}&appid={OPEN_WEATHER_KEY}&units=metric"
            )
            if data.status_code == "400":
                break
            checked_city ={
                "city_id": city,
                "checked": True,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"]
            }

            col.replace_one(
                filter={"city_id": city}, replacement=checked_city
            )

            # if we take more than 60s, we kill this process and let the new one do the job
            if time.time() - t1 >= 60:
                break


if __name__ == "__main__":
    scan_db_and_get_cites_data()
