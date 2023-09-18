from devgrid_api.exceptions import DatabaseError
from devgrid_api.mongodb.mongodb import MongoConnection
from devgrid_api.settings import REST_FRAMEWORK


def get_paginated_data_query(
    database: str = None,
    collection: str = None,
    query: dict = {},
    projection: dict = {},
    page: int = 1,
    page_size: int = None,
):
    if not page_size:
        page_size = REST_FRAMEWORK["page_size"]
    try:
        with MongoConnection() as mongo:
            col = mongo.get_db_collection(database, collection)
            count = col.count_documents(query)
            data = col.aggregate(
                [
                    {"$match": query},
                    {"$addFields": {"id": {"$toString": "$_id"}}},
                    {
                        "$project": {
                            "_id": False,
                        }
                        | projection
                    },
                    {
                        "$skip": (page - 1)
                        * page_size  # No. of documents to skip (should be 0 for page 1)
                    },
                    {"$limit": page_size},
                ]
            )
            return count, list(data)
    except Exception as e:
        raise DatabaseError(details=str(e))
