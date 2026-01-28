kullanici_adi = "Ramazan"
sifre = "1234"

def login():
    hak = 3

    while hak > 0:
        girilen_kullanici = input("Kullanıcı adı: ").strip()
        girilen_sifre = input("Şifre: ").strip()

        if kullanici_adi == girilen_kullanici and sifre == girilen_sifre:
            print("Giriş başarılı.")
            return True
        else:
            hak = hak - 1
            if hak > 0:
                print(f" Hatalı giriş. Kalan hak: {hak}")
            else:
                print(" Hak bitti. Program kapanıyor.")
                return False

def main():
    sonuc = login()
    if sonuc:
        print(" Menüye geçilebilir (login=True).")
    else:
        print(" Menü açılmayacak (login=False).")

if __name__ == "__main__":
    main()