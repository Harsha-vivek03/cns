import numpy as np

def matrix_modulo_inverse(matrix, modulo):
    det = int(np.linalg.det(matrix))
    det_inverse = pow(det, -1, modulo)
    adjugate = (det_inverse * np.round(det * np.linalg.inv(matrix))).astype(int)
    return (adjugate % modulo + modulo) % modulo

def encrypt(message, key_matrix):
    message_vector = np.array([ord(char) - ord('A') for char in message])
    encrypted_vector = np.dot(message_vector, key_matrix) % 26
    encrypted_message = ''.join([chr(val + ord('A')) for val in encrypted_vector])
    return encrypted_message

def decrypt(encrypted_message, key_matrix):
    key_matrix_inverse = matrix_modulo_inverse(key_matrix, 26)
    encrypted_vector = np.array([ord(char) - ord('A') for char in encrypted_message])
    decrypted_vector = np.dot(encrypted_vector, key_matrix_inverse) % 26
    decrypted_message = ''.join([chr(val + ord('A')) for val in decrypted_vector])
    return decrypted_message

# Example usage:
key_matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
message = "PAY"

# Encryption
encrypted_message = encrypt(message, key_matrix)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, key_matrix)
print("Decrypted message:", decrypted_message)
