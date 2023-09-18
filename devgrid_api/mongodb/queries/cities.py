from devgrid_api.exceptions import DatabaseError, ItemNotFound
from devgrid_api.mongodb.mongodb import MongoConnection
from pymongo.collection import ReturnDocument


def get_cities_that_are_in_db(
    database: str = None,
    collection: str = None,
    cities: list = [],
    query: dict = {}
) -> list:
    query = [
        {
            "$match": {
                "city_id": {"$in": cities}
            } | query
        },
        {
            "$group": {
                "_id": None,
                "city_ids": {"$addToSet": "$city_id"}
            }
        },
        {
            "$project": {"_id": False, "city_ids": True}
        },
    ]
    with MongoConnection() as mongo:
        collection = mongo.get_db_collection(database, collection)

        data = list(collection.aggregate(query))

    return data


def get_latest_sixty_unchecked_cities(
    database: str = None,
    collection: str = None,
) -> list:
    query = [
        {
            "$match": {"checked": False}
        },
        {
            "$sort": {"_id": -1}
        },
        {
            "$limit": 60,
        },
        {
            "$group": {
                "_id": None,
                "city_ids": {"$addToSet": "$city_id"}
            }
        },
        {
            "$project": {"_id": False, "city_ids": True}
        },
    ]
    with MongoConnection() as mongo:
        collection = mongo.get_db_collection(database, collection)
        data = list(collection.aggregate(query))

    return data
