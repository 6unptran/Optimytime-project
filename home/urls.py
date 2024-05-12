from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('requests_msg/', views.requests_msg, name='requests_msg')
]