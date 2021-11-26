# import path
from os import name
from django.conf.urls import url
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:category_slug>/", views.store, name="products_by_category"),
]
