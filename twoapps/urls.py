from django.urls import path
from . import views

urlpatterns= [
    path('twoapps/', views.twoapps, name='twoapps'),
]