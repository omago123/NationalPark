from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mapApp'


urlpatterns = [
    path('state/', views.state2 , name='mountain'),
    path('state/main/', views.stateMain , name='state'),

    path('map/', views.map , name='map'),
    path('map/<int:id>/', views.choice_state , name='map_detail'),

    path('course/create/', views.form_creat , name='creat'),
    path('state/create/', views.state_creat , name='state_creat'),
]