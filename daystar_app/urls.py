from django.contrib import admin
from django.urls import path
from daystar_app.views import *



urlpatterns = [
    path('', homePage, name="home"),
    path('babies/', babiesList, name="babies"),
    path('sitters/', sittersList, name="sitters"),
    path('payments/', payments, name="payments"),
    path('procurement/', payments, name="procurement"),
]