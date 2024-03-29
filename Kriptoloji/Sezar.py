def caesar_cipher(message, mode):
    key = 3  # Sabit anahtar değeri
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    translated_message = ""

    if mode == 'd':
        key = -key

    for char in message:
        if char in alphabet:
            # Karakterin alfabe içindeki indeksini buluyoruz
            index = alphabet.index(char)
            # Şifreleme/çözme için indeksi kaydırıyoruz
            shifted_index = (index + key) % len(alphabet)
            # Kaydırılmış indekse karşılık gelen karakteri alıyoruz
            translated_message += alphabet[shifted_index]
        else:
            translated_message += char

    return translated_message

def main():
    mode = input("Encrypt or Decrypt? (e or d): ")
    message = input("Enter a message: ")

    if mode not in ['e', 'd']:
        print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")
        return

    result = caesar_cipher(message, mode)
    print("Result:", result)

def caesar_cipher(message, mode):
    key = 3  # Sabit anahtar değeri
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    translated_message = ""

    if mode == 'd':
        key = -key

    for char in message:
        if char in alphabet:
            # Karakterin alfabe içindeki indeksini buluyoruz
            index = alphabet.index(char)
            # Şifreleme/çözme için indeksi kaydırıyoruz
            shifted_index = (index + key) % len(alphabet)
            # Kaydırılmış indekse karşılık gelen karakteri alıyoruz
            translated_message += alphabet[shifted_index]
        else:
            translated_message += char

    return translated_message

def main():
    mode = input("Encrypt or Decrypt? (e or d): ")
    message = input("Enter a message: ")
    message = message.replace(" ", "")
    
    if mode not in ['e', 'd']:
        print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")
        return

    result = caesar_cipher(message, mode)
    print("Result:", result)

if __name__ == "__main__":
    main()

