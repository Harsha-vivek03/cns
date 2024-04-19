def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_length = len(key)
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length]) - ord('A')
        if plaintext[i].isupper():
            encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
        elif plaintext[i].islower():
            encrypted_char = chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = plaintext[i]
        ciphertext += encrypted_char
    return ciphertext

def main():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
