from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home),
    path('region/', views.region),
    path('region/<int:id>', views.region),
    path('park/<int:id>', views.park),
    path('park_list/', views.park_list),
]
