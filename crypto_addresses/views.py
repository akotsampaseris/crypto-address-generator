from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination


from crypto_addresses.models import CryptoAddress
from crypto_addresses.services import CryptoAddressService
from crypto_addresses.serializers import (
    CryptoAddressDetailsSerializer, 
    CryptoAddressListSerializer
)

# Create your views here.
class AddressList(APIView, PageNumberPagination):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'
    page_query_param = 'page'

    def get(self, request, format=None):
        page_size = request.query_params.get('page_size')
        if page_size: self.page_size = int(page_size)

        coin_id = request.query_params.get('coin_id')
        if coin_id:
            addresses = CryptoAddress.objects.filter(
                coin__id=coin_id
            )
        else:
            addresses = CryptoAddress.objects.all()
        
        page = self.paginate_queryset(
            addresses, 
            request, 
            view=self
        )

        serializer = CryptoAddressListSerializer(
            page, 
            many=True
        )

        return self.get_paginated_response(
            serializer.data
        )


class AddressDetails(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def get(self, request, id, format=None):
        address = get_object_or_404(CryptoAddress, id=id)
        serializer = CryptoAddressDetailsSerializer(address)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class GenerateAddress(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        coin_id = request.query_params.get('coin_id')

        if not coin_id:
            error_msg = 'No coin selected.'

            return Response(
                error_msg,
                status=status.HTTP_400_BAD_REQUEST
            )

        address = CryptoAddressService\
            .create_crypto_address(coin_id)
        
        serializer = CryptoAddressDetailsSerializer(address)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
        