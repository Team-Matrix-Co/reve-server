def encrypt_password(password):
    encrypted_password = ""
    for char in password:
        # Shift each character by 1 position in the ASCII table
        encrypted_char = chr(ord(char) + 1)
        encrypted_password += encrypted_char
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = ""
    for char in encrypted_password:
        # Shift each character back by 1 position in the ASCII table
        decrypted_char = chr(ord(char) - 1)
        decrypted_password += decrypted_char
    return decrypted_password
