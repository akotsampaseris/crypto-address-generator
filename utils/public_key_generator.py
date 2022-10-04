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
        private_key_bytes = codecs.decode(
            private_key.strip(), 'hex'
        )
        
        sk = SigningKey.from_string(
                private_key_bytes, 
                curve=SECP256k1
            )

        vk = sk.verifying_key
        public_key = vk.to_string()

        return codecs.encode(public_key, 'hex')