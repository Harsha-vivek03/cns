
def encrypt(message, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = [''] * len(key)
    for i, k in enumerate(key_order):
        for j in range(i, len(message), len(key)):
            cipher_text[k] += message[j]
    return ''.join(cipher_text)

def decrypt(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = -(-len(cipher_text) // num_columns)  # Ceiling division
    plain_text = [''] * num_rows
    index = 0
    for i in range(num_columns):
        col = key_order.index(i)
        for j in range(num_rows):
            if index < len(cipher_text):
                plain_text[j] += cipher_text[index]
                index += 1
    return ''.join(plain_text)

def main():
    message = input("Enter the message to be encrypted: ").replace(" ", "").upper()
    key = input("Enter the encryption key: ").replace(" ", "").upper()
    
    cipher_text = encrypt(message, key)
    print("Encrypted message:", cipher_text)
    
    decrypted_message = decrypt(cipher_text, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
