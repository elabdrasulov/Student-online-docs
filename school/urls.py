from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('register/student/', StudentRegisterView.as_view()),
    # path('login/director/', DirectorRegisterView.as_view())
]