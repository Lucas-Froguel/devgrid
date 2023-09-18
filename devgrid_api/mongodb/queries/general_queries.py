from devgrid_api.exceptions import DatabaseError, ItemNotFound
from devgrid_api.mongodb.mongodb import MongoConnection
from pymongo.collection import ReturnDocument


def get_documents_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
):
    try:
        with MongoConnection() as mongo:
            data = mongo.get_db_collection(database, collection).find(query)
            return list(data)
    except Exception as e:
        raise DatabaseError(details=str(e))


def get_documents_with_projection_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
    projection: dict = None
):
    try:
        with MongoConnection() as mongo:
            data = mongo.get_db_collection(database, collection).find(
                query, projection=projection
            )
            return list(data)
    except Exception as e:
        raise DatabaseError(details=str(e))


def get_all_documents_query(database: str = None, collection: str = None):
    try:
        with MongoConnection() as mongo:
            data = mongo.get_all_collection_documents(database, collection)
            return list(data)
    except Exception as e:
        raise DatabaseError(details=str(e))


def get_all_documents_with_projection_query(
    database: str = None, collection: str = None, projection: dict = None
):
    try:
        with MongoConnection() as mongo:
            data = mongo.get_db_collection(database, collection).find(
                projection=projection
            )
            return list(data)
    except Exception as e:
        raise DatabaseError(details=str(e))


def get_one_document_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
    projection: dict = {},
    convert_id: bool = False,
    raise_exception: bool = True
):
    with MongoConnection() as mongo:
        col = mongo.get_db_collection(database, collection)
        item = col.find_one(query, projection=projection)
        if item:
            if convert_id:
                item["_id"] = str(item["_id"])
            return item
        if raise_exception:
            raise ItemNotFound(details=str(query))


def update_one_document_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
    newvalues: dict = None,
):
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            obj = col.update_one(query, newvalues)
            return obj
    except Exception as e:
        raise DatabaseError(details=str(e))


def insert_one_document_query(
    database: str = None, collection: str = None, data: dict = None
):
    try:
        with MongoConnection() as mongo:
            obj = mongo.insert_document(
                db_name=database,
                collection_name=collection,
                document=data
            )
            return str(obj.inserted_id)
    except Exception as e:
        raise DatabaseError(details=str(e))


def bulk_insert_documents_query(
    database: str = None, collection: str = None, data: list = None
):
    try:
        with MongoConnection() as mongo:
            mongo.bulk_insert_documents(
                db_name=database,
                collection_name=collection,
                documents=data
            )
    except Exception as e:
        raise DatabaseError(details=str(e))


def soft_delete_one_document_query(
    database: str = None, collection: str = None, query: dict = None
):
    del_value = {"is_active": False, "is_deleted": True}
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            obj = col.update_one(query, del_value)
            return obj
    except Exception as e:
        raise DatabaseError(details=str(e))


def delete_all_documents_query(database: str = None, collection: str = None):
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            col.delete_many({})
    except Exception as e:
        raise DatabaseError(details=str(e))


def find_and_update_one_document_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
    newvalues: dict = None,
    projection: dict = None,
):
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            obj = col.find_one_and_update(
                query,
                newvalues,
                projection=projection,
                return_document=ReturnDocument.AFTER,
            )
            return obj
    except Exception as e:
        raise DatabaseError(details=str(e))


def bulk_update_document_query(
    database: str = None,
    collection: str = None,
    query: dict = None,
    newvalues: dict = None,
):
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            obj = col.update_many(
                query,
                newvalues,
            )
            return obj
    except Exception as e:
        raise DatabaseError(details=str(e))
