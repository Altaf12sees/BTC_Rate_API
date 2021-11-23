from rest_framework import serializers
from APP001.models import models


class serializationClassModel(serializers.ModelSerializer):
    class Meta:
        model=models.BTCPrice
        fields='__all__'