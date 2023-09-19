import mongomock
from devgrid_api.mongodb.queries.cities import get_cities_that_are_in_db, get_latest_sixty_unchecked_cities


def test_get_cities_that_are_in_db(monkeypatch):
    db = "db"
    col = "col"
    collection = mongomock.MongoClient().db.col

    objects = [
        dict(city_id=k) for k in range(10)
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id
    query = {}

    monkeypatch.setattr(
        "devgrid_api.mongodb.queries.general_queries.MongoConnection.get_db_collection",
        lambda x, y, z: collection,
    )
    response = get_cities_that_are_in_db(
        database=db, collection=col, query=query, cities=[1, 2, 3, 20]
    )

    assert isinstance(response, list)
    assert response == [{"city_ids": [1, 2, 3]}]


def test_get_latest_sixty_unchecked_cities(monkeypatch):
    db = "db"
    col = "col"
    collection = mongomock.MongoClient().db.col

    objects = [
        dict(city_id=k, checked=False if k%2 else True) for k in range(10)
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id

    monkeypatch.setattr(
        "devgrid_api.mongodb.queries.general_queries.MongoConnection.get_db_collection",
        lambda x, y, z: collection,
    )
    response = get_latest_sixty_unchecked_cities(
        database=db, collection=col
    )

    assert isinstance(response, list)
    assert response == [{"city_ids": [9, 7, 5, 3, 1]}]
