from rest_framework import serializers

from . import models

class CryptoCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CryptoCoin
        fields = ['id', 'name']