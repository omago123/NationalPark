from django.contrib import admin
from django.urls import path
import contact.views as views

urlpatterns = [
    path('', views.contact),
]