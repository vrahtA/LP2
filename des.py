from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


key = get_random_bytes(8)  
print("Randomly Generated Key:", key)

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)  
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(cipher_text)
    decrypted = unpad(decrypted_padded, DES.block_size)
    return decrypted.decode()

message = "HELLODES"
print("Original Message:", message)

encrypted = des_encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = des_decrypt(encrypted, key)
print("Decrypted:", decrypted)
