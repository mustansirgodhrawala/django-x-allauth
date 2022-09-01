from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('private_data', views.private_data, name="private_data"),
]
