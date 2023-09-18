from dataclasses import dataclass

from django.utils.translation import gettext_lazy as _
from rest_framework import status as http_status

from devgrid_api.mixins.exceptions import ExceptionMixin


@dataclass
class UserNotFound(ExceptionMixin):
    _message: str = _("Could not find any user with the provide data.")
    status: int = http_status.HTTP_404_NOT_FOUND


@dataclass
class UserAlreadyPresent(ExceptionMixin):
    _message: str = _("User already has posted cities.")
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class ValidationError(ExceptionMixin):
    _message: str = _("Something went wrong.")
    details: str = ""
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class DatabaseError(ExceptionMixin):
    _message: str = _("Something went wrong while connecting to the database.")
    details: str = ""
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class MetadataError(ExceptionMixin):
    _message: str = _("Something went wrong while updating the metadata.")
    details: str = ""
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class ItemNotFound(ExceptionMixin):
    _message: str = _("Item not found.")
    details: str = ""
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class PageNotAnInteger(ExceptionMixin):
    _message: str = _("Page is not an integer.")
    status: int = http_status.HTTP_400_BAD_REQUEST


@dataclass
class EmptyPage(ExceptionMixin):
    _message: str = _("Empty page.")
    status: int = http_status.HTTP_400_BAD_REQUEST
