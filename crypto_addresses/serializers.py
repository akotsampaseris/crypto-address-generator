from rest_framework import serializers

from . import models

class CryptoAddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CryptoAddress
        fields = ['id', 'coin', 'address']


class CryptoAddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CryptoAddress
        fields = '__all__'