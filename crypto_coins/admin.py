from django.contrib import admin

from . import models

@admin.register(models.CryptoCoin)
class CryptoCoinAdmin(admin.ModelAdmin):
    pass

