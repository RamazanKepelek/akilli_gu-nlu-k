# main.py
# Telefon rehberi projesinin ana dosyası.
# Giriş başarılı olursa menü açılır, kullanıcı çıkış yapana kadar döner.

import auth
import phonebook
import raffle
import logger


def menu():
    while True:
        print("\n--- MENÜ ---")
        print("1- Kişi Ekle")
        print("2- Kişi Sil")
        print("3- Kişi Ara")
        print("4- Rehberi Listele")
        print("5- Çekiliş Yap")
        print("6- Çıkış")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            phonebook.kisi_ekle()
            logger.log_yaz("Kişi eklendi")

        elif secim == "2":
            phonebook.kisi_sil()
            logger.log_yaz("Kişi silindi")

        elif secim == "3":
            phonebook.kisi_ara()
            logger.log_yaz("Kişi arandı")

        elif secim == "4":
            phonebook.rehberi_listele()
            logger.log_yaz("Rehber listelendi")

        elif secim == "5":
            raffle.cekilis_yap()
            logger.log_yaz("Çekiliş yapıldı")

        elif secim == "6":
            print("Çıkış yapılıyor...")
            logger.log_yaz("Programdan çıkış")
            break

        else:
            print("Geçersiz seçim. 1-6 arası gir.")


def main():
    if auth.login():
        print("Menüye geçiliyor...")
        menu()
    else:
        print("Program kapanıyor...")


if __name__ == "__main__":
    main()
