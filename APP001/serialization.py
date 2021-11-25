from rest_framework import serializers
from . import models


class SerializationClassModel(serializers.ModelSerializer):
    class Meta:
        model=models.BTCPrice
        fields = '__all__'
    
    # def create(self, validated_data):
    #     return models.BTCPrice.objects.create(**validated_data)