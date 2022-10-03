import sha3
import codecs
from utils import encryptions

from utils.private_key_generator import PrivateKeyGenerator
from utils.public_key_generator import PublicKeyGenerator

class Wallet:
    encryption = 'secp256k1'

    @classmethod
    def generate_wallet(cls):
        private_key = PrivateKeyGenerator\
            .strong_random_number()

        public_key = PublicKeyGenerator\
            .generate_public_key(
                private_key, 
                encryption=cls.encryption
            )

        public_key_hash = cls.keccak(public_key)
        wallet = '0x' + public_key_hash[-40:]
        
        return wallet


    @staticmethod
    def keccak(public_key):
        keccak256 = sha3.keccak_256()
        keccak256.update(codecs.decode(public_key, 'hex'))

        return keccak256.hexdigest()