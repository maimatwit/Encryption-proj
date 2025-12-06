import os #https://compile7.org/encryption-decryption/how-to-use-chacha20-256-to-encrypt-and-decrypt-in-python/
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305



def ChaCha20_en( message):
    key =os.urandom(32)
    Chacha20 = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    if isinstance(message, str):
        message = message.encode()
    ciphertext = Chacha20.encrypt(nonce, message, None)
    return key, nonce, ciphertext

def ChaCha20_de(key, nonce, ciphertext):
    Chacha20 = ChaCha20Poly1305(key)
    plaintext = Chacha20.decrypt(nonce, ciphertext, None)
    return plaintext

def ChaCha20_ed(message):
    key =os.urandom(32)
    nonce = os.urandom(12)# number once 
    Chacha20 = ChaCha20Poly1305(key)

    ciphertext = nonce + Chacha20.encrypt(nonce, message.encode(), None)
    plaintext = Chacha20.decrypt(ciphertext[:12],ciphertext[12:],None)
    return key.hex(), ciphertext.hex(), plaintext.decode()





if __name__ == "__main__":
    #print(ChaCha20_ed("Tesing test"))
    message = "Message for ChaCha20 encryption"
    key, nonce, ciphertext = ChaCha20_en(message)
    print("Ciphertext: ",ciphertext.hex())
    decrypt = ChaCha20_de(key, nonce, ciphertext)
    print("Decrypted text: ", decrypt.decode())