from Crypto.Cipher import AES #From: https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from secrets import token_bytes
import time

#timer

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

key = token_bytes(16)

@timer
def encrypt(msg): 
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce #a unqiue number used once
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag
@timer
def decrypt(nonce, ciphertext,tag):
    cipher = AES.new(key,AES.MODE_EAX,nonce = nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")
    except:
        return False
    
nonce, ciphertext, tag = encrypt(input("Enter a message: "))

plaintext = decrypt(nonce,ciphertext, tag)
print(f'Cipher text:  {ciphertext}')
if not plaintext:
    print('Message corrupted')
else:
    print(f'Plain text: {plaintext}')