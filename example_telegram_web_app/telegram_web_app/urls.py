from django.urls import path

from .views import click_coin, get_points, index


urlpatterns = [
    path("", index, name="index"),
    path("api/click_coin", click_coin, name="click_coin"),
    path("api/get_points", get_points, name="get_points"),
]
