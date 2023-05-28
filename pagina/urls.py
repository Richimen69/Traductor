from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('integrantes/', views.integrantes),
]