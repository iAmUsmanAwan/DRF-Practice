from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'transaction_type'] # we can specify the fields that we want to serialize and show in the API response
        # if we want to show all the fields in the model, we can use fields = '__all__' instead of specifying each field individually
        # we can also use exclude = ['id'] to exclude the id field from the API response

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
