# raffle.py
# çekiliş burada
# rehber boşsa çekiliş olmaz, doluysa rastgele seçer

import random
import phonebook


def cekilis_yap():
    if len(phonebook.rehber) == 0:
        print("Rehber boş. Çekiliş yapılamaz.")
        return

    isimler = list(phonebook.rehber.keys())
    kazanan = random.choice(isimler)

    print("\n--- ÇEKİLİŞ ---")
    print(f"Kazanan: {kazanan} -> {phonebook.rehber[kazanan]}")