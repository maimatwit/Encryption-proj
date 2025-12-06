import secrets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def aes_en( message):
    key = os.urandom(32)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    if isinstance(message, str):
        message = message.encode()
    ciphertext = aes.encrypt(nonce, message, None)
    return key, nonce, ciphertext
#symmetric encryption
def aes_ed(message):
    key =secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)# number once 
    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce, message.encode(), None)
    plaintext = aes.decrypt(ciphertext[:12],ciphertext[12:],None)
    return key.hex(), ciphertext.hex(), plaintext.decode()

def aes_de(key, nonce, ciphertext):
    
    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return plaintext

if __name__ == "__main__":
    #print(aes_ed("AES test"))
    message = "Message for AES encryption"
    key, nonce, ciphertext = aes_en(message)
    print("Ciphertext: ",ciphertext.hex())
    decrypt = aes_de(key, nonce, ciphertext)
    print("Decrypted text: ", decrypt.decode())