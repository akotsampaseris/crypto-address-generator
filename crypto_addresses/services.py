from django.shortcuts import get_object_or_404

from crypto_addresses.models import CryptoAddress
from crypto_coins.models import CryptoCoin

class CryptoAddressService:
    @classmethod
    def create_crypto_address(cls, coin_id=None):
        coin = get_object_or_404(CryptoCoin, id=coin_id)
        wallet, private_key = cls.generate_wallet_address(coin_id)
        crypto_address = CryptoAddress(
            coin=coin,
            address=wallet,
            private_key=private_key,
        )

        crypto_address.save()

        return crypto_address


    @staticmethod
    def generate_wallet_address(coin_id):
        from importlib import import_module

        wallet_module_path = 'crypto_addresses.utils.wallets.%s' % (coin_id)
        wallet_module = import_module(wallet_module_path)
        wallet_class = getattr(wallet_module, 'Wallet')

        
        wallet, private_key = wallet_class.generate_wallet()

        return wallet, private_key
