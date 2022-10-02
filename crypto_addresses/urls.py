from django.urls import path, include

from . import views

app_name = 'crypto_addresses'
urlpatterns = [
    path('addresses/', include([
        path(
            '', 
            views.AddressList.as_view(), 
            name='address-list'
        ),
        path(
            'address/<int:id>', 
            views.AddressDetails.as_view(), 
            name='address-details'
        ),
        path(
            'generate/', 
            views.GenerateAddress.as_view(), 
            name='generate-address'
        ),
    ]))
]