from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from file_manager import *
import binascii


def encrypt_message():
    # Leer archivo
    msg = bytes(open_read_file("message.txt"), encoding='utf8')
    
    #   Abrir llave publica A
    f = open('publicKey_A.pem','r')
    pubKey_B = RSA.importKey(f.read())
    publicKey_B = pubKey_B.publickey()
    f.close()

    #   Cifrar usando llave publica A
    encryptor = PKCS1_OAEP.new(publicKey_B)
    encrypted = encryptor.encrypt(msg)
    
    #   Escribit txt
    f = open('message_C.txt','wb')
    f.write(encrypted)


def decrypt_message():   
    #   Leer archivo cifrado
    f = open("message_C.txt", 'rb')
    msg = f.read()

    #   Abrir llave privada A
    f = open('privateKey_A.pem','r')
    privKey_A = RSA.importKey(f.read())
    
    #   Decifrar con privada A
    cipher = PKCS1_OAEP.new(privKey_A)
    message = cipher.decrypt(msg)

    #   Escribir mensaje 
    f = open('message_C_D.txt','w')
    f.write(str(message))


def main():
    encrypt_message()
    decrypt_message()

main()
