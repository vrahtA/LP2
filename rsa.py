import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(msg, public):
    enc = []
    e, n = public
    for c in msg:
        enc.append(pow(ord(c), e, n))
    return enc

def decrypt(enc, private):
    dec = []
    d, n = private
    for c in enc:
        dec.append(chr(pow(c, d, n)))
    return ''.join(dec)

p, q = 43, 53 
public_key, private_key = generate_keys(p, q)
message = input()
print("Public key", public_key)
print("Private key", private_key)
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Encrypted Message: ",encrypted_message,"     Decrypted Message:",decrypted_message)
