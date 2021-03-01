from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

publicKey_B = open("publicKey_B.pem")
publicKey_B = RSA.importKey(publicKey_B)

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(publicKey_B)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))