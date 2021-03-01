from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from file_manager import *
import binascii


def encrypt_message_public_B():
    msg = bytes(open_read_file("message.txt"), encoding='utf8')
    
    #   Cifrar con publicKey B
    f = open('publicKey_B.pem','r')
    pubKey_B = RSA.importKey(f.read())
    publicKey_B = pubKey_B.publickey()

    encryptor = PKCS1_OAEP.new(publicKey_B)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))
    return binascii.hexlify(encrypted)

def encrypt_message_private_A(msg):   
    #   Cifrar con privateKey A
    f = open('privateKey_A.pem','r')
    privKey_A = RSA.importKey(f.read())
    
    encryptor = PKCS1_OAEP.new(privKey_A)
    encrypted_msg = encryptor.encrypt(msg)
    print(encrypted_msg)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(encoded_encrypted_msg)
    return encoded_encrypted_msg


def main():
    encryted = encrypt_message_public_B()
    encrypt_message_private_A(encryted)

main()

# msg = b'A message for encryption'

# encryptor = PKCS1_OAEP.new(publicKey_B)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", encrypted)


# f = open('privateKey_B.pem','r')
# priKey_B = RSA.importKey(f.read())

# decryptor = PKCS1_OAEP.new(priKey_B)
# decrypted = decryptor.decrypt(encrypted)
# print('Decrypted:', decrypted)