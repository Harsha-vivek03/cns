def encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = alphabet.index(char.upper())
            encrypted_char = key[char_index]
            encrypted_text += encrypted_char.upper() if is_upper else encrypted_char.lower()
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = key.index(char.upper())
            decrypted_char = alphabet[char_index]
            decrypted_text += decrypted_char.upper() if is_upper else decrypted_char.lower()
        else:
            decrypted_text += char

    return decrypted_text

def main():
    choice = input("Do you want to perform encryption or decryption? (Enter 'e' for encryption, 'd' for decryption): ")

    if choice.lower() == 'e':
        plaintext = input("Enter the text to encrypt: ")
        key = input("Enter the substitution key (26 characters, no duplicates): ")

        if len(key) != 26 or not key.isalpha() or len(set(key.upper())) != 26:
            print("Invalid key. The key must be 26 unique alphabetical characters.")
            return

        result = encrypt(plaintext, key)
        print(f"Encrypted text: {result}")

    elif choice.lower() == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        key = input("Enter the substitution key (26 characters, no duplicates): ")

        if len(key) != 26 or not key.isalpha() or len(set(key.upper())) != 26:
            print("Invalid key. The key must be 26 unique alphabetical characters.")
            return

        result = decrypt(ciphertext, key)
        print(f"Decrypted text: {result}")

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
