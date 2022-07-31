import random
import time

secenekler = ("taş","kağıt","makas")

tas = secenekler[0]
kagıt = secenekler[1]
makas = secenekler[2]
puan = 0

print("\n\nTaş kağıt makas oyununa hoşgeldiniz ! ")
while True:
    secim = input("\ntaş kağıt makas ? \nOyundan çıkmak için '*' a basın :  ")
    randomSecim = random.choice(secenekler)
    if ((randomSecim == tas and secim == kagıt) or (randomSecim == makas and secim == tas) or (randomSecim == kagıt and secim == makas)):
        print(f"""
    Tebrikler kazandınız !
    Sizin seçiminiz : {secim}
    Bilgisayar secimi : {randomSecim}
            """)
        puan += 1
    elif randomSecim == secim :
        print(f"""
    Aynı seçim
    Sizin seçiminiz : {secim}
    Bilgisayar secimi : {randomSecim}
                """)
        pass
    elif ((randomSecim == kagıt and secim == tas) or (randomSecim == tas and secim == makas) or (randomSecim == makas and secim == kagıt)):
        print(f"""
    Kaybettiniz !!
    Sizin seçiminiz : {secim}
    Bilgisayar secimi : {randomSecim}
    """)
        puan -= 1
    elif secim == '*':
        print("Çıkış yapılıyor ..")
        time.sleep(2)
        break
    else:
        print("Geçersiz seçim !")
print("\nBilgisayara karşı puanınız : ",puan)