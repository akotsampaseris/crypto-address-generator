from django.urls import path, include

from . import views

app_name = 'crypto_coins'
urlpatterns = [
    path('coins/', include([
        path(
            '',
            views.CoinList.as_view(),
            name='coin-list'
        ),
        path(
            'new/',
            views.AddCoin.as_view(),
            name='new'
        )
    ]))
]