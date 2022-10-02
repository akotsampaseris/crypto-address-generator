from django.db import models

class CryptoCoin(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'coin'
        verbose_name_plural = 'coins'