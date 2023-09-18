from django.urls import include, path

from .v1.router import urlpatterns as v1_router


urlpatterns = [
    path("", include(v1_router)),
]
