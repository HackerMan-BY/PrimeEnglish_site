from django.urls import path
from . import views

urlpatterns = [
    path('', views.frst, name="main"),
    path('contacts/', views.contact, name="contacts"),
    path('lessons/', views.lessons, name="lessons"),
]