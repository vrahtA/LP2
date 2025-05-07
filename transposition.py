import math

def encrypt(text, key):
    text = text.replace(" ", "").upper()
    rows = math.ceil(len(text) / key)
    matrix = [text[i:i+key] for i in range(0, len(text), key)]
    return ''.join(''.join(row[c] for row in matrix if c < len(row)) for c in range(key))

def decrypt(cipher, key):
    cols = key
    rows = math.ceil(len(cipher) / key)
    short_cols = key - (len(cipher) % key) if len(cipher) % key != 0 else 0

    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for c in range(cols):
        num_chars = rows - (1 if c >= cols - short_cols else 0)
        for r in range(num_chars):
            matrix[r][c] = cipher[idx]
            idx += 1

    return ''.join(''.join(row) for row in matrix)

# Input
text = input("Enter the text: ")
key = int(input("Enter the key (integer): "))

# Output
encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("\nOriginal Text: ", text.replace(" ", "").upper())
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
