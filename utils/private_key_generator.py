import secrets
import codecs

class PrivateKeyGenerator:
    @staticmethod
    def strong_random_number(bits_size=256):
        bits = secrets.randbits(bits_size)
        bits_hex = hex(bits)
        private_key = bits_hex[2:]
        
        return private_key