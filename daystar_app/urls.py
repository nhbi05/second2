from django.contrib import admin
from django.urls import path
from daystar_app.views import *



urlpatterns = [
    path('', homePage, name="home"),
    path('students/', studentsList, name="students"),
    path('courses/', courseList, name="courses"),
    path('transactions/', transactions, name="transactions"),
]