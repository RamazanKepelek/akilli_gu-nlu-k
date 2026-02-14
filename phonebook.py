# phonebook.py
# rehber işleri burada
# kişi ekle / sil / ara (.get) / listele
# dosyaya kaydet / dosyadan yükle (readlines)

rehber = {}  # {"isim": "telefon"}


def dosyadan_yukle():
    # data.txt varsa rehberi oradan dolduruyoruz
    # satır formatı: isim|telefon
    global rehber
    rehber = {}

    try:
        dosya = open("data.txt", "r", encoding="utf-8")
        satirlar = dosya.readlines()
        dosya.close()
    except FileNotFoundError:
        # dosya yoksa sorun değil, boş rehberle başlar
        return

    for satir in satirlar:
        satir = satir.strip()
        if satir == "":
            continue

        parca = satir.split("|", 1)
        if len(parca) != 2:
            continue

        isim = parca[0].strip()
        tel = parca[1].strip()

        if isim != "" and tel != "":
            rehber[isim] = tel


def dosyaya_kaydet():
    # rehberi data.txt dosyasına yazıyoruz
    dosya = open("data.txt", "w", encoding="utf-8")
    for isim, tel in rehber.items():
        dosya.write(f"{isim}|{tel}\n")
    dosya.close()


def kisi_ekle():
    # isim ve telefon alıp rehbere ekliyoruz
    isim = input("İsim (Ad Soyad): ").strip()
    tel = input("Telefon: ").strip()

    if isim == "" or tel == "":
        print("Boş bilgi olmaz.")
        return

    # aynı isim varsa üstüne yazar (basit tuttum)
    rehber[isim] = tel
    dosyaya_kaydet()
    print("Kişi kaydedildi.")


def kisi_sil():
    # isim alıp rehberden siliyoruz
    isim = input("Silinecek kişinin adı: ").strip()

    if isim == "":
        print("İsim boş olamaz.")
        return

    if isim in rehber:
        rehber.pop(isim)
        dosyaya_kaydet()
        print("Kişi silindi.")
    else:
        print("Bu isim rehberde yok.")


def kisi_ara():
    # .get() ile arıyoruz
    isim = input("Aranacak kişinin adı: ").strip()

    if isim == "":
        print("İsim boş olamaz.")
        return

    tel = rehber.get(isim)
    if tel is None:
        print("Bulunamadı.")
    else:
        print(f"{isim} -> {tel}")


def rehberi_listele():
    # rehberi ekrana basıyoruz
    if len(rehber) == 0:
        print("Rehber boş.")
        return

    print("\n--- REHBER ---")
    for isim, tel in rehber.items():
        print(f"{isim} : {tel}")


# program başında dosyadan yükleyelim
dosyadan_yukle()