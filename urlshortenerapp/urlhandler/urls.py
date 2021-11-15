from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('<str:query>/', views.look_up, name="look_up")
]
