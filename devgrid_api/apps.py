from django.apps import AppConfig as DjangoConfig


class AppConfig(DjangoConfig):
    name = "devgrid_api"
    verbose_name = "DevgridApi"
