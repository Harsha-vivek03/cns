def encrypt_rail_fence(plaintext, rails):
    matrix = [[' ' for _ in range(len(plaintext))] for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row, col = 0, 0

    for char in plaintext:
        matrix[row][col] = char
        row += direction

        if row == rails - 1 or row == 0:
            direction = -direction

        col += 1

    ciphertext = ''.join(''.join(row) for row in matrix)
    return ciphertext

def decrypt_rail_fence(ciphertext, rails):
    matrix = [[' ' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = 1
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        matrix[row][col] = 'X'
        row += direction

        if row == rails - 1 or row == 0:
            direction = -direction

        col += 1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if matrix[i][j] == 'X':
                matrix[i][j] = ciphertext[index]
                index += 1

    plaintext = ''
    direction = 1
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        plaintext += matrix[row][col]
        row += direction

        if row == rails - 1 or row == 0:
            direction = -direction

        col += 1

    return plaintext

def main():
    choice = input("Do you want to perform encryption or decryption? (Enter 'e' for encryption, 'd' for decryption): ")

    if choice.lower() == 'e':
        plaintext = input("Enter the text to encrypt: ")
        rails = int(input("Enter the number of rails: "))
        result = encrypt_rail_fence(plaintext, rails)
        print(f"Encrypted text: {result}")

    elif choice.lower() == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        rails = int(input("Enter the number of rails: "))
        result = decrypt_rail_fence(ciphertext, rails)
        print(f"Decrypted text: {result}")

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
