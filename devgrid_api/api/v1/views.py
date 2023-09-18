from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from devgrid_api.usecases import add_user_cities_to_cities_collection, add_user_and_cities_to_user_collection, \
    get_user_cities_percentage
from .serializers import UserSerializer, UserAndCitiesSerializer, ResponsePercentageSerializer


@api_view(["POST"])
def receive_user_and_cities_view(request: Request) -> Response:
    serializer = UserAndCitiesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data_id = add_user_and_cities_to_user_collection(serializer.data)
    add_user_cities_to_cities_collection(serializer.data["cities"])

    return Response(serializer.data | {"_id": data_id}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_user_percentage_of_completeness_and_city_data_view(request: Request) -> Response:
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    percentage = get_user_cities_percentage(user_id=serializer.data["user_id"])

    response_serializer = ResponsePercentageSerializer(
        data={"user_id": serializer.data["user_id"], "percentage": percentage}
    )
    response_serializer.is_valid(raise_exception=True)

    return Response(response_serializer.data, status=status.HTTP_200_OK)
