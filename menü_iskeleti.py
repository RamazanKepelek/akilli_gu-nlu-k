def menu():
    while True:
        print("\n--- MENÜ ---")
        print("1 - Su Tüketimi Ekle")
        print("2 - Sağlık Durumu Gir")
        print("3 - Haftalık Rapor")
        print("4 - Ruh Hali Analizi")
        print("5 - Çıkış")

        secim = input("Seçimin: ").strip()

        if secim == "1":
            print("Seçenek 1 çalıştı")

        elif secim == "2":
            print("Seçenek 2 çalıştı")

        elif secim == "3":
            print("Seçenek 3 çalıştı")

        elif secim == "4":
            print("Seçenek 4 çalıştı")

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("⚠️ Lütfen 1 ile 5 arasında bir değer giriniz.")