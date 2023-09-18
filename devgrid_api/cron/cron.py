
from devgrid_api.settings import MONGODB_NAME, MONGO_USERS_COLLECTION, MONGO_CITIES_DATA_COLLECTION]
from devgrid_api.mongodb.queries.general_queries import insert_one_document_query, bulk_insert_documents_query, \
    get_one_document_query

def scan_db_and_get_city_data():
