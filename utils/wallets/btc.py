import codecs
import hashlib
import base58

from utils.private_key_generator import PrivateKeyGenerator
from utils.encryptions import secp256k1

class Wallet:
    @classmethod
    def generate_wallet(cls):
        private_key = PrivateKeyGenerator\
            .strong_random_number()
        
        public_key = secp256k1.Encryption\
            .generate_public_key(private_key)

        compressed_public_key = \
            cls.compress_public_key(public_key)
        
        public_key_hash = cls.hash160(compressed_public_key)
        network_public_key = \
            cls.convert_to_network_public_key(
                public_key_hash,
                testnet=False
            )
        
        checksum = cls.checksum(network_public_key)
        network_address = network_public_key + checksum
        wallet = cls.base58(network_address)

        return wallet


    @staticmethod
    def compress_public_key(public_key):
        public_key_X = public_key[:len(public_key)//2]
        
        #X_last_byte = int(public_key_X[-1], 16) 
        bitcoin_byte = b'03'
        
        compressed_public_key = bitcoin_byte \
            + public_key_X
        
        return compressed_public_key


    @staticmethod
    def hash160(public_key):
        sha256 = hashlib.sha256(
            codecs.decode(public_key, 'hex')
        )
        
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(sha256.digest())

        public_key_hash = ripemd160.digest()
        
        return codecs.encode(public_key_hash, 'hex')


    @staticmethod
    def convert_to_network_public_key(public_key_hash, testnet=False):
        # Add network prefix to public key
        network_prefix = b'6f' if testnet else b'00'
        network_public_key = network_prefix + public_key_hash

        return network_public_key


    @staticmethod
    def checksum(network_public_key):
        # Run sha256 twice to get checksum
        sha256_once = hashlib.sha256(
            codecs.decode(network_public_key, 'hex')
        )
        sha256_twice = hashlib.sha256(sha256_once.digest())

        hash = sha256_twice.digest()
        checksum = hash[:4]

        return codecs.encode(checksum, 'hex')

    
    @staticmethod
    def base58(network_address):
        wallet = base58.b58encode(
            codecs.decode(network_address, 'hex'), 
            alphabet=base58.BITCOIN_ALPHABET
        ).decode('utf-8')

        print(wallet)

        return wallet



    