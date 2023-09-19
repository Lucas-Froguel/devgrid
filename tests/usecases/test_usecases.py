import bson
from devgrid_api.usecases import add_user_cities_to_cities_collection, get_user_cities_percentage, \
    add_user_and_cities_to_user_collection


def mock_get_cities_that_are_in_db(**kwargs):
    return [{"city_ids": kwargs["cities"][::-2]}]


def mock_bulk_insert_documents_query(**kwargs):
    pass


def mock_get_one_document_query(**kwargs):
    return {"cities": [i for i in range(20)]}


def mock_get_cities_that_are_in_db(**kwargs):
    return [{"city_ids": [i for i in range(9)]}]



def test_add_user_cities_to_cities_collection(cities_data, monkeypatch):
    monkeypatch.setattr(
        "devgrid_api.usecases.get_cities_that_are_in_db", mock_get_cities_that_are_in_db
    )
    monkeypatch.setattr(
        "devgrid_api.usecases.bulk_insert_documents_query", mock_bulk_insert_documents_query
    )

    add_user_cities_to_cities_collection(cities_data)


def test_get_user_cities_percentage(monkeypatch):
    monkeypatch.setattr(
        "devgrid_api.usecases.get_one_document_query", mock_get_one_document_query
    )
    monkeypatch.setattr(
        "devgrid_api.usecases.get_cities_that_are_in_db", mock_get_cities_that_are_in_db
    )

    percentage = get_user_cities_percentage("ABCD")

    assert percentage == 100 * (9/20)


def test_add_user_and_cities_to_user_collection(monkeypatch):
    _id = str(bson.ObjectId())

    monkeypatch.setattr(
        "devgrid_api.usecases.get_one_document_query", lambda **kwargs: None
    )
    monkeypatch.setattr(
        "devgrid_api.usecases.insert_one_document_query", lambda **kwargs: _id
    )

    response_id = add_user_and_cities_to_user_collection({"user_id": "ABCD"})

    assert response_id == _id
