def affine_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((3 * (ord(char) - base) + 12) % 26) + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter plaintext: ")
    encrypted_text = affine_encrypt(plaintext)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
