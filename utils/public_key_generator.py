import codecs
from ecdsa import SigningKey, SECP256k1

class PublicKeyGenerator:
    @classmethod
    def generate_public_key(cls, private_key, encryption: str = None):
        use = f"use_{encryption}"

        if hasattr(cls, use) \
            and callable(func := getattr(cls, use)):
            
            return func(private_key)

    @staticmethod
    def use_secp256k1(private_key=None):
        sk = SigningKey.from_string(
                codecs.decode(private_key, 'hex'), 
                curve=SECP256k1
            )

        vk = sk.verifying_key
        public_key = vk.to_string()

        return codecs.encode(public_key, 'hex')