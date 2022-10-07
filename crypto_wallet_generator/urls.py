from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include([
        path('', include('crypto_addresses.urls')),
        path('', include('crypto_coins.urls')),
    ])),
]
