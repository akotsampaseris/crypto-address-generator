from django.contrib import admin

from . import models

@admin.register(models.CryptoAddress)
class CryptoAddressAdmin(admin.ModelAdmin):
    pass