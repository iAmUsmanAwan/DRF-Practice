from django.urls import path
from expense import views

urlpatterns = [
    path('get-transactions/', views.GetTransactions, name='get-transactions'),   # http://127.0.0.1:8000/api/get-transactions/
]