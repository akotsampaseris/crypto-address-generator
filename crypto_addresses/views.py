from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from . import serializers
from . import models

# Create your views here.
class AddressList(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    address_model = models.CryptoAddress
    address_serializer = serializers.CryptoAddressListSerializer

    def get(self, request, format=None):
        addresses = self.address_model.objects.all()
        serializer = self.address_serializer(addresses, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class AddressDetails(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    address_model = models.CryptoAddress
    address_serializer = serializers.CryptoAddressDetailsSerializer

    def get(self, request, id, format=None):
        address = get_object_or_404(self.address_model, id=id)
        serializer = self.address_serializer(address)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class GenerateAddress(APIView):
    parser_classes = [JSONParser, ]
    renderer_classes = [JSONRenderer, ]
    address_model = models.CryptoAddress
    address_serializer = serializers.CryptoAddressListSerializer


    def get(self, request, format=None):
        id = 1

        if id:
            address = self.address_model.object.get(id=id)
        else:
            error_msg = 'No id was provided.'
            
            return Response(
                error_msg,
                status=status.HTTP_400_BAD_REQUEST
            )


        if address:
            serializer = self.address_serializer(address)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            error_msg = 'No address found.'

            return Response(
                error_msg,
                status=status.HTTP_404_NOT_FOUND
            )