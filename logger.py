# logger.py
# yaptığımız işlemleri log.txt dosyasına yazıyoruz
# log yazılamazsa program bozulmasın diye sessiz geçiyoruz

from datetime import datetime


def log_yaz(mesaj):
    zaman = datetime.now().strftime("%d-%m-%Y %H:%M")

    try:
        dosya = open("log.txt", "a", encoding="utf-8")
        dosya.write(f"[{zaman}] {mesaj}\n")
        dosya.close()
    except:
        pass