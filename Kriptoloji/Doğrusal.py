def linear_cipher_encrypt(text, key1, key2):
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    encrypted_text = ''

    for char in text:
        if char.isalpha():
            if char.islower():
                index = (alphabet.index(char) * key1 + key2) % 29
                encrypted_text += alphabet[index]
            else:
                index = (alphabet.index(char.lower()) * key1 + key2) % 29
                encrypted_text += alphabet[index].upper()
        else:
            encrypted_text += char

    return encrypted_text

def linear_cipher_decrypt(encrypted_text, key1, key2):
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    decrypted_text = ''

    mod_inv = _modinv(key1, 29)

    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                index = (mod_inv * (alphabet.index(char) - key2)) % 29
                decrypted_text += alphabet[index]
            else:
                index = (mod_inv * (alphabet.index(char.lower()) - key2)) % 29
                decrypted_text += alphabet[index].upper()
        else:
            decrypted_text += char

    return decrypted_text

def _modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def main():
    choice = input("Enter 'e' to encrypt a message, 'd' to decrypt: ")
    if choice == 'e':
        text = input("Enter the message to encrypt: ")
        key1 = int(input("Enter the first key value (an integer): "))
        key2 = int(input("Enter the second key value (an integer): "))
        print("Encrypted Text:", linear_cipher_encrypt(text, key1, key2))
    elif choice == 'd':
        encrypted_text = input("Enter the encrypted message: ")
        key1 = int(input("Enter the first key value (an integer): "))
        key2 = int(input("Enter the second key value (an integer): "))
        print("Decrypted Text:", linear_cipher_decrypt(encrypted_text, key1, key2))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
