from django.contrib import admin
from django.urls import path

from start.views import *

urlpatterns = [
    path('', f_start),
]
