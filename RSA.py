from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii



f = open('publicKey_B.pem','r')
pubKey_B = RSA.importKey(f.read())
publicKey_B = pubKey_B.publickey()

msg = b'A message for encryption'

encryptor = PKCS1_OAEP.new(publicKey_B)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", encrypted)


f = open('privateKey_B.pem','r')
priKey_B = RSA.importKey(f.read())

decryptor = PKCS1_OAEP.new(priKey_B)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)