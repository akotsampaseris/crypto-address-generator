from tabnanny import verbose
from django.db import models

from crypto_coins.models import CryptoCoin

class CryptoAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
        
    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'