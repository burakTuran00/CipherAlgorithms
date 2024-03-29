def sifrele(metin, k):
    sifreli_metin = ''
    for karakter in metin:
        if karakter.isalpha():
            if karakter.islower():
                indis = (alfabe.find(karakter) + k) % 29
                sifreli_metin += alfabe[indis]
            else:
                indis = (alfabe.find(karakter.lower()) + k) % 29
                sifreli_metin += alfabe[indis].upper()
        else:
            sifreli_metin += karakter
    return sifreli_metin

def sifre_coz(sifreli_metin, k):
    return sifrele(sifreli_metin, -k)

alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

def main():
    secim = input("Metni şifrelemek için 'e', şifreyi çözmek için 'd' girin: ")
    if secim == 'e':
        metin = input("Şifrelemek istediğiniz metni girin: ")
        metin = metin.replace(" ", "")
        k = int(input("Kaç harf kaydırma yapmak istediğinizi belirtin: "))
        print("Şifreli Metin:", sifrele(metin, k))
    elif secim == 'd':
        sifreli_metin = input("Çözmek istediğiniz şifreli metni girin: ")
        k = int(input("Kaç harf kaydırıldığını belirtin: "))
        print("Orijinal Metin:", sifre_coz(sifreli_metin, k))
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
