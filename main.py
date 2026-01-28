USERNAME = "ramazan"
PASSWORD = "1234"

# 7 günlük su tüketimi listesi (ml)
# index 0 = 1. gün, index 6 = 7. gün
su_listesi = [0, 0, 0, 0, 0, 0, 0]


def login():
    # Kullanıcı giriş yapabiliyor mu onu kontrol eden fonksiyon.
    # Doğruysa True döner ve menüye girilir.
    # Yanlışsa hak azalır, hak bitince False döner.

    hak = 3

    while hak > 0:
        u = input("Kullanıcı adı: ").strip()
        p = input("Şifre: ").strip()

        # strip() kullanmamın sebebi başına / sonuna boşluk girilirse sorun çıkmaması
        if u == USERNAME and p == PASSWORD:
            print("Giriş başarılı.")
            return True

        hak -= 1
        if hak > 0:
            print(f"Hatalı giriş. Kalan hak: {hak}")
        else:
            print("Hak bitti. Program kapanıyor.")
            return False


def su_girisi_al():
    # Bu fonksiyon sadece kullanıcıdan gün ve ml bilgisini alıyor.
    # Listeye ekleme işlemini burada değil menü tarafında yapıyorum.

    while True:
        try:
            gun = int(input("Lütfen gün giriniz (1-7): ").strip())

            # Gün aralığı kontrolü
            if gun < 1 or gun > 7:
                print("1 ile 7 arasında bir gün gir.")
                continue

            ml = int(input("Lütfen kaç ml su içtiğini gir: ").strip())

            # 0 veya negatif değer mantıksız olduğu için kabul etmiyorum
            if ml <= 0:
                print("0'dan büyük bir değer gir.")
                continue

            # Buraya geldiysek veri doğru demektir
            return gun, ml

        except ValueError:
            # Harf veya saçma bir şey girilirse buraya düşer
            print("Sadece sayı girmen gerekiyor.")
            continue


def su_tuketimi_ekle(gun, miktar=0):
    # Koçun istediği default parametre örneği burada.
    # miktar gönderilmezse otomatik olarak 0 kabul edilir.

    # Kullanıcı günleri 1-7 giriyor ama liste 0-6 olduğu için -1 yapıyoruz
    index = gun - 1

    # Aynı güne tekrar veri girilirse üstüne eklenmesi için += kullanıyoruz
    su_listesi[index] += miktar


def haftalik_rapor_uret():
    # Haftalık su verilerinden basit bir özet çıkarıyorum.

    toplam = 0
    for deger in su_listesi:
        toplam += deger

    gun_sayisi = len(su_listesi)

    if toplam == 0:
        return "Bu hafta hiç su kaydı yok."

    ortalama = toplam / gun_sayisi

    # En iyi ve en kötü günü manuel olarak buluyorum
    max_deger = su_listesi[0]
    min_deger = su_listesi[0]
    en_iyi_index = 0
    en_kotu_index = 0

    i = 0
    for deger in su_listesi:
        if deger > max_deger:
            max_deger = deger
            en_iyi_index = i

        if deger < min_deger:
            min_deger = deger
            en_kotu_index = i

        i += 1

    # index 0 = gün 1 olduğu için +1 yapıyoruz
    en_iyi_gun = en_iyi_index + 1
    en_kotu_gun = en_kotu_index + 1

    # Raporu string olarak biriktiriyorum
    rapor = "---- HAFTALIK SU RAPORU ----\n"
    rapor += f"Veriler: {su_listesi}\n"
    rapor += f"Toplam: {toplam} ml\n"
    rapor += f"Ortalama: {ortalama:.2f} ml\n"
    rapor += f"En iyi gün: {en_iyi_gun} (Değer: {max_deger} ml)\n"
    rapor += f"En kötü gün: {en_kotu_gun} (Değer: {min_deger} ml)"

    return rapor


def ruh_hali_analizi():
    # Kullanıcıdan kısa bir cümle alıyorum.
    # Sonra kelimelerin ilk harflerini çıkarıyorum.
    # Amaç string ve döngü pratiği yapmak.

    metin = input("Bugünkü ruh halini tek cümleyle yaz: ").strip()

    if metin == "":
        return "Boş cümle girdin."

    kelimeler = metin.split()

    # join kullanmadan düz döngüyle biriktiriyorum
    sonuc = ""
    for kelime in kelimeler:
        if kelime != "":
            sonuc += kelime[0]

    return "Kelime baş harfleri: " + sonuc


def menu():
    # Menü sürekli döner. Kullanıcı 5 seçince çıkar.

    while True:
        print("\n-- MENÜ --")
        print("1 - Su Tüketimi Ekle")
        print("2 - Sağlık Durumu")
        print("3 - Haftalık Rapor")
        print("4 - Ruh Hali Analizi")
        print("5 - Çıkış")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            # Kullanıcıdan veri al
            gun, ml = su_girisi_al()

            # Veriyi fonksiyon üzerinden listeye ekle
            su_tuketimi_ekle(gun, ml)

            print(f"Gün {gun} için {ml} ml eklendi. Gün toplamı: {su_listesi[gun-1]} ml")

        elif secim == "2":
            # Basit sağlık yorumu: seçilen günün su miktarına göre
            try:
                gun = int(input("Hangi gün? (1-7): ").strip())

                if gun < 1 or gun > 7:
                    print("1-7 arası bir gün gir.")
                    continue

                index = gun - 1
                deger = su_listesi[index]

                if deger < 1500:
                    print("Su tüketimin yetersiz.")
                elif deger <= 2500:
                    print("Su tüketimin normal.")
                else:
                    print("Su tüketimin iyi, böyle devam.")

            except ValueError:
                print("Sayı girmen gerekiyor.")

        elif secim == "3":
            # Haftalık raporu ekrana bas
            print(haftalik_rapor_uret())

        elif secim == "4":
            print(ruh_hali_analizi())

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. 1-5 arası gir.")


def main():
    # Önce login, başarılıysa menüye gir
    if login():
        menu()


if __name__ == "__main__":
    main()