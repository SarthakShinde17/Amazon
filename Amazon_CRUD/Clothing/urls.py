from django.urls import path
from Clothing import views

urlpatterns = [
    path("", views.home, name="home"),
]