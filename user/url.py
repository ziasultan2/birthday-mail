from django.urls import path
from user import views

urlpatterns = [
    path('seed', views.seed),
]