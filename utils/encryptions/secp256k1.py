import codecs
from ecdsa import SigningKey, SECP256k1

class Encryption:
    @staticmethod
    def generate_public_key(private_key=None):
        sk = SigningKey.from_string(
                bytes.fromhex(private_key), 
                curve=SECP256k1
            )

        vk = sk.verifying_key
        public_key = vk.to_string()

        return codecs.encode(public_key, 'hex')