def encrypt(text, key):
    # Türk alfabesi
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'

    # Anahtarın uzunluğunu al
    key_length = len(key)
    # Metni anahtara göre böl
    splitted_text = [text[i:i+key_length] for i in range(0, len(text), key_length)]

    # Anahtarın harf değerleriyle metni şifrele
    encrypted_text = ''
    for i, chunk in enumerate(splitted_text):
        for j, char in enumerate(chunk):
            # Anahtar harfinin alfabedeki indisini al
            key_index = alphabet.find(key[j])
            # Metin harfinin alfabedeki indisini al
            text_index = alphabet.find(char)
            # Şifrele ve mod 29 al
            encrypted_index = (key_index + text_index ) % 29
            # Şifrelenmiş harfi alfabeden bul ve şifreli metine ekle
            encrypted_text += alphabet[encrypted_index]
        # Her anahtar bölümü için ayracı ekleyelim
        encrypted_text += 'a'

    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ").lower()  # Metni küçük harfe çeviriyoruz
    text = text.replace(" ", "")
    key = input("Enter the key: ").lower()  # Anahtarı küçük harfe çeviriyoruz
    encrypted_text = encrypt(text, key)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()
