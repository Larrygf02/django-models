from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate-pdf/', views.some_view)
]