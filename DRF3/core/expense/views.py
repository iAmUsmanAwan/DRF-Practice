from django.shortcuts import render
from expense.serializers import TransactionSerializer
from .models import Transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def GetTransactions(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset, many=True)

    return Response(serializer.data)