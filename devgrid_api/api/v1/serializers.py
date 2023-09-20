from rest_framework import serializers
from rest_framework.serializers import Serializer


class UserSerializer(Serializer):
    user_id = serializers.CharField(max_length=100)


class ResponsePercentageSerializer(Serializer):
    percentage = serializers.CharField(max_length=7)
    user_id = serializers.CharField(max_length=100)


class UserAndCitiesSerializer(Serializer):
    user_id = serializers.CharField(max_length=100)
    cities = serializers.ListField(child=serializers.CharField(max_length=7, min_length=7))
