from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers

class CoinList(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    model_class = models.CryptoCoin
    serializer_class = serializers.CryptoCoinListSerializer

    def get(self, request, format=None):
        coins = self.model_class.objects.all()
        serializer = self.serializer_class(coins, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class AddCoin(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    model_class = models.CryptoCoin
    serializer_class = serializers.CryptoCoinListSerializer

    def get(self, request, format=None):
        coins = self.model_class.objects.all()
        serializer = self.serializer_class(coins, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )