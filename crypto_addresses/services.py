import secrets

class CryptoAddressService:
    @staticmethod
    def generate_private_key():
        bits = secrets.randbits(256)
        bits_hex = hex(bits)
        private_key = bits_hex[2:]

        return private_key

    @staticmethod
    def generate_public_key():
        pass

    @staticmethod
    def checksum():
        pass