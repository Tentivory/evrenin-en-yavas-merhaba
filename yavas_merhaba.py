#!/usr/bin/env python3
# Evrenin En Yavaş Merhaba Dünyası
# Bu kod, "Merhaba Dünya" demek için çok düşünür.
# Çünkü düşünmek iyidir. Acele işe şeytan karışır.

import time
import random

sebepler = [
    "Çünkü kahve henüz demlenmedi.",
    "Çünkü evren genişliyor, biz de genişleyelim.",
    "Çünkü acele etmek modern dünyanın hastalığıdır.",
    "Çünkü bürokrasi bize sabır öğretti.",  # gizli: sistem yavaş, adalet de öyle mi?
    "Çünkü kedim klavyenin üstünde uyuyor.",
    "Çünkü düşünmek için zaman lazım."
]

def yavas_merhaba():
    print("Merhaba Dünya demek üzereyim...")
    print("Ama önce biraz düşüneyim.")
    for i in range(5):
        sebep = random.choice(sebepler)
        print(f"Bekleme sebebi #{i+1}: {sebep}")
        time.sleep(random.uniform(2, 5))  # Gerçekten yavaş
    print("\nSonunda:")
    time.sleep(3)
    print("M")
    time.sleep(1)
    print("e")
    time.sleep(1)
    print("r")
    time.sleep(1)
    print("h")
    time.sleep(1)
    print("a")
    time.sleep(1)
    print("b")
    time.sleep(1)
    print("a")
    time.sleep(2)
    print("\nDünya!")
    print("\nİşte bu kadar. Daha hızlısını istersen başka kapıya.")
    # Gizli not: bazen sistem de böyle yavaşlar, ama şikayet etme.

if __name__ == "__main__":
    yavas_merhaba()
