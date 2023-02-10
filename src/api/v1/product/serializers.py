from rest_framework import serializers


class CreateSessionSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField(max_length=3)
    name_product = serializers.CharField(max_length=64)
    quantity = serializers.IntegerField(required=False)