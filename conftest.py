import pytest
from bson.decimal128 import Decimal128
from faker import Faker

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def api_client_with_credentials(user, api_client):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def fake():
    return Faker("en")


@pytest.fixture
def labors_mongo_format(faker, budget):
    return [
        {
            "_id": "633d82843fd06fc61e8b34a9",
            "labor_type": "MASON",
            "budget": "UUID(217f05dc-a5b4-48d7-b145-768a65f3ed4b)",
            "price": 100,
            "pricing_type": "DAILY",
            "target_area": 15.00,
            "completion_time_type": "DAY",
            "completion_time": 15,
            "subtotal": Decimal128('1500')
        },
        {
            "_id": "633d82fedb0f9bff766b22bb",
            "labor_type": "MASON",
            "budget": "UUID(217f05dc-a5b4-48d7-b145-768a65f3ed4b)",
            "price": 200,
            "pricing_type": "CONTRACT",
            "target_area": 40.00,
            "completion_time_type": "MONTH",
            "completion_time": 20,
            "subtotal": Decimal128('200')
        },
    ]

