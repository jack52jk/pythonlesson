from django.urls import path

from . import views

urlpatterns = [
    path('login', views.LoginShowView),
    path('auth', views.LoginView),
]