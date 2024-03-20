def permute(text, key, permutation):
    # Metni parçalara böler
    chunks = [text[i:i+key] for i in range(0, len(text), key)]
    # Eksik karakterleri 'a' ile doldurur
    for i in range(len(chunks[-1]), key):
        chunks[-1] += 'a'
    # Şifrelenmiş metni tutmak için boş bir string oluşturur
    encrypted_text = ''

    # Her parça için permütasyon uygular
    for chunk in chunks:
        # Parçadaki karakterlerin sırasını değiştirmek için permütasyonu kullanır
        permuted_chunk = ''
        for i in range(len(permutation)):
            index = int(permutation[i]) - 1
            if index < len(chunk):
                permuted_chunk += chunk[index]
        # Şifrelenmiş metne ekler
        encrypted_text += permuted_chunk

    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    key = int(input("Enter the key length: "))
    permutation = input("Enter the permutation (e.g., 32541): ")

    # Permütasyon anahtarının doğruluğunu kontrol eder
    if sorted(permutation) != sorted([str(i) for i in range(1, key + 1)]):
        print("Invalid permutation key!")
        return

    encrypted_text = permute(text, key, permutation)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()
