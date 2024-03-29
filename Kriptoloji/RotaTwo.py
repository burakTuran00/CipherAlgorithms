def decode_and_print(input_str, key):
    # Matris boyutlarını hesapla
    rows = -(-len(input_str) // key)  # Yukarıya yuvarlamak için -(-x // y) kullanılır.
    cols = key

    # Matrisi oluştur
    matrix = [[''] * cols for _ in range(rows)]

    # Matrise harfleri yerleştir
    index = 0
    i = 0
    j = 0
    direction = 0  # 0: sağa, 1: aşağı, 2: sola, 3: yukarı

    while index < len(input_str):
        # Harfi matrise yerleştir
        matrix[i][j] = input_str[index]
        index += 1

        # Yönü güncelle
        if direction == 0:
            if j + 1 == cols or matrix[i][j + 1] != '':
                direction = 1
                i += 1
            else:
                j += 1
        elif direction == 1:
            if i + 1 == rows or matrix[i + 1][j] != '':
                direction = 2
                j -= 1
            else:
                i += 1
        elif direction == 2:
            if j == 0 or matrix[i][j - 1] != '':
                direction = 3
                i -= 1
            else:
                j -= 1
        elif direction == 3:
            if i == 0 or matrix[i - 1][j] != '':
                direction = 0
                j += 1
            else:
                i -= 1

    # Her satırı bir metne ekleyip yazdır
    print("Şifrelenmiş Matris:")
    for row in matrix:
        print(row)
    
    decoded_text = ""
    for row in matrix:
        decoded_row = ''.join(row)
        decoded_text += decoded_row

    print("Çözülen Metin:")
    print(decoded_text)

# Kullanıcıdan metni al
input_text = input("Metni girin: ")
input_text = input_text.replace(" ", "")
# Kullanıcıdan anahtar al
key = int(input("Bir anahtar girin (tam sayı): "))

# Metni çöz ve sonucu yazdır
decode_and_print(input_text, key)
