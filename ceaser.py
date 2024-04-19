def encrypt(plaintext, key):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

def main():
    choice = input("Do you want to perform encryption or decryption? (Enter 'e' for encryption, 'd' for decryption): ")

    if choice.lower() == 'e':
        plaintext = input("Enter the text to encrypt: ")
        key = int(input("Enter the key for encryption: "))
        result = encrypt(plaintext, key)
        print(f"Encrypted text: {result}")

    elif choice.lower() == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        key = int(input("Enter the key for decryption: "))
        result = decrypt(ciphertext, key)
        print(f"Decrypted text: {result}")

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
