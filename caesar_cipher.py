def cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += encrypted_char
            elif char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                result += encrypted_char
        else:
            result += char
    return result

def decipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
                result += decrypted_char
            elif char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
                result += decrypted_char
        else:
            result += char
    return result

def main():
    
    original_text = input("Enter the input String to Encrypt: ")
    key = int(input("Enter the key to Encrypt: "))

    encrypted_text = cipher(original_text, key)
    print("Original message:", original_text)
    print("Encrypted message:", encrypted_text.upper())

    decrypted_text = decipher(encrypted_text, key)
    print("Decrypted message:", decrypted_text)

main()
