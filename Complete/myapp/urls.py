from django.urls import path
from .views import add_data, view_data

urlpatterns = [
    path('add-data/', add_data, name='add_data'),
    path('view-data/', view_data, name='view_data'),
]
