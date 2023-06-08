import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    insan1 = Insan("12345678912", "Ömer", "Çıtak", 28, "Erkek", "Türk")
    insan2 = Insan("98765432198", "Feyza", "Kır", 32, "Kadın", "Türk")
    print("İnsanlar: ")
    print(insan1)
    print(insan2)
except Exception as e:
    print("Hata:", e)

try:
    issiz1 = Issiz("45678912345", "Veli", "Yiğit", 42, "Erkek", "Türk", {"beyaz yaka": 1, "mavi yaka": 2, "yönetici": 3})
    issiz2 = Issiz("41414141414", "Merve", "Arslan", 40, "Kadın", "Türk", {"mavi yaka": 3, "yönetici": 2})
    issiz3 = Issiz("63636363636", "Caner", "Şahin", 28, "Erkek", "Türk", {"beyaz yaka": 2, "mavi yaka": 1})
    print("\nİşsizler: ")
    print(issiz1)
    print(issiz2)
    print(issiz3)
except Exception as e:
    print("Hata:", e)

try:
    calisan1 = Calisan("52635263526", "Nehir", "Erdem", 30, "Kadın", "Türk", "Inşaat", 3, 7000)
    calisan2 = Calisan("47878787878", "Salih", "Uçan", 33, "Erkek", "Türk", "Teknoloji", 6, 17000)
    calisan3 = Calisan("91191191191", "İpek", "Alın", 32, "Kadın", "Türk", "Muhasebe", 3, 8000)
    print("\nCalisanlar: ")
    print(calisan1)
    print(calisan2)
    print(calisan3)
except Exception as e:
    print("Hata:", e)

try:
    mavi_yaka1 = MaviYaka("19071907190", "Hasan", "Ali", 34, "Erkek", "Türk", "Teknoloji", 3, 16000, 0.4)
    mavi_yaka2 = MaviYaka("10101010101", "Ece", "Vural", 35, "Kadın", "Türk", "Diğer", 3, 13000, 0.3)
    mavi_yaka3 = MaviYaka("12121212121", "Samet", "Özdemir", 40, "Erkek", "Türk", "Teknoloji", 7, 26000, 1.0)
    print("\nMavi yakalılar: ")
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)
except Exception as e:
    print("Hata:", e)

try:
    beyaz_yaka1 = BeyazYaka("85296396385", "Kardelen", "Kutlu", 32, "Kadın", "Türk", "Diğer", 3, 8000, 1000)
    beyaz_yaka2 = BeyazYaka("36363636363", "Arda", "Güler", 33, "Erkek", "Türk", "Teknoloji", 7, 29000, 1500)
    beyaz_yaka3 = BeyazYaka("74185274852", "Selin", "Yıldız", 35, "Kadın", "Türk", "Muhasebe", 6, 18000, 1200)
    print("\nBeyaz Yakalılar: ")
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
except Exception as e:
    print("Hata:", e)