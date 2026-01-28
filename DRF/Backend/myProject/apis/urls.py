from django.urls import path
from . import views

urlpatterns = [
    # this url will be the last part of the url
    # http://127.0.0.1:8000/api/get-data
    path('get-data/', views.getData),  
    path('add-item/', views.addItem),
]