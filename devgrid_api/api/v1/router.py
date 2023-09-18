# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path
from rest_framework import routers
from .views import (
    receive_user_and_cities_view,
    get_user_percentage_of_completeness_and_city_data_view
)

router = routers.DefaultRouter()

urlpatterns = [
    path("add_cities/", receive_user_and_cities_view),
    path("get_cities/", get_user_percentage_of_completeness_and_city_data_view)
]

urlpatterns += router.urls