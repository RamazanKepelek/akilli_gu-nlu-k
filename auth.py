# auth.py
# sadece giriş işi burada
# users.txt içinden şifreyi alıp kontrol ediyoruz

def login():
    # users.txt yoksa giriş yapamayız
    try:
        dosya = open("users.txt", "r", encoding="utf-8")
        kayitli_sifre = dosya.readline().strip()
        dosya.close()
    except FileNotFoundError:
        print("users.txt bulunamadı.")
        return False

    hak = 3  # 3 deneme hakkı

    while hak > 0:
        girilen = input("Lütfen şifrenizi giriniz: ").strip()

        if girilen == kayitli_sifre:
            print("Giriş başarılı.")
            return True

        hak -= 1
        if hak > 0:
            print(f"Şifre yanlış. Kalan hak: {hak}")

    print("Deneme hakkınız bitti. Giriş başarısız.")
    return False