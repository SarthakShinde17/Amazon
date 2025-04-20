from django.urls import path
from Clothing import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update/<int:id>", views.update_data, name="update_data"),
    path("delete/<int:id>", views.delete_data, name="delete_data"), 

]