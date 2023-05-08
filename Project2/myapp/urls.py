from django.urls import path
from .views import input_view, success_view

urlpatterns = [
    path('input/', input_view, name='input'),
    path('success/', success_view, name='success'),
]
