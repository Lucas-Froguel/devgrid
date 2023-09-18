import datetime

from devgrid_api.mongodb.queries.general_queries import insert_one_document_query, bulk_insert_documents_query, \
    get_one_document_query
from devgrid_api.mongodb.queries.cities import get_cities_that_are_in_db
from devgrid_api.settings import MONGODB_NAME, MONGO_USERS_COLLECTION, MONGO_CITIES_DATA_COLLECTION
from devgrid_api.exceptions import UserAlreadyPresent


def add_user_cities_to_cities_collection(cities: list):
    # make sure there is no repetition in the list that will be saved on the db
    cities = list(set(cities))

    cities_in_db = get_cities_that_are_in_db(
        database=MONGODB_NAME,
        collection=MONGO_CITIES_DATA_COLLECTION,
        cities=cities
    )
    if cities_in_db:
        cities_in_db = cities_in_db[0]["city_ids"]

    formatted_cities = []
    for city in cities:
        if city in cities_in_db:
            continue
        formatted_cities.append(
            {
                "city_id": city,
                "checked": False,
                "temperature": None,
                "humidity": None
            }
        )

    if formatted_cities:
        bulk_insert_documents_query(
            database=MONGODB_NAME,
            collection=MONGO_CITIES_DATA_COLLECTION,
            data=formatted_cities
        )


def add_user_and_cities_to_user_collection(request_data: dict) -> dict:

    user = get_one_document_query(
        database=MONGODB_NAME,
        collection=MONGO_USERS_COLLECTION,
        query={"user_id": request_data["user_id"]},
        raise_exception=False
    )
    if user:
        raise UserAlreadyPresent()

    data_id = insert_one_document_query(
        database=MONGODB_NAME,
        collection=MONGO_USERS_COLLECTION,
        data=request_data | {"datetime": datetime.datetime.now()}
    )

    return data_id


def get_user_cities_percentage(user_id: str) -> dict:
    user = get_one_document_query(
        database=MONGODB_NAME,
        collection=MONGO_USERS_COLLECTION,
        query={"user_id": user_id},
        raise_exception=True
    )

    cities_in_db = get_cities_that_are_in_db(
        database=MONGODB_NAME,
        collection=MONGO_CITIES_DATA_COLLECTION,
        cities=user["cities"],
        query={"checked": True}
    )

    percentage = 100 * (len(cities_in_db) / len(user["cities"]))

    return percentage

