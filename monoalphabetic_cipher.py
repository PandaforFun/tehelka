import random
import string

def generate_cipher_key():
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return {string.ascii_uppercase[i]: alphabet[i] for i in range(26)}

def encrypt(message, cipher_key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += cipher_key[char]
            else:
                encrypted_message += cipher_key[char.upper()].lower()
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, cipher_key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            for key, value in cipher_key.items():
                if char.upper() == value:
                    decrypted_message += key.lower() if char.islower() else key
                    break
        else:
            decrypted_message += char
    return decrypted_message

def main():
    cipher_key = generate_cipher_key()
    
    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt(message, cipher_key)
    print("Encrypted message:", encrypted_message.upper())

    decrypted_message = decrypt(encrypted_message, cipher_key)
    print("Decrypted message:", decrypted_message)

main()
