# Simple RSA for text

# Step 1: Choose two primes
p = 3
q = 11

# Step 2: Compute n and phi
n = p * q             # n = 33
phi = (p - 1) * (q - 1)  # phi = 20

# Step 3: Choose public exponent e
e = 7  # Small prime that is coprime to phi

# Step 4: Compute private key d (modular inverse of e mod phi)
def modinv(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

d = modinv(e, phi)

# Step 5: Encryption (convert each char to int and encrypt)
def encrypt_text(message):
    return [(ord(char) ** e) % n for char in message]

# Step 6: Decryption (decrypt each int and convert back to char)
def decrypt_text(cipher):
    return ''.join([chr((char ** d) % n) for char in cipher])

# Example usage
text = "HELLOWORLD"
ciphertext = encrypt_text(text)
decrypted = decrypt_text(ciphertext)

# Output
print("Public key: ", (e, n))
print("Private key:", (d, n))
print("Original text:", text)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted)


