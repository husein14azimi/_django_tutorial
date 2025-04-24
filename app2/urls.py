from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app2homepage),
    path('temp/', views.app2temp),
]