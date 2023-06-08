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

# DataFrame oluşturma
data = {
    "nesne_degeri": ["çalışan", "mavi yaka", "beyaz yaka"] * 3,
    "tc_no": ["52635263526", "19071907190", "85296396385", "47878787878", "10101010101", "36363636363",
              "91191191191", "12121212121", "74185274852"],
    "ad": ["Nehir", "Hasan", "Kardelen", "Salih", "Ece", "Arda", "İpek", "Samet", "Selin"],
    "soyad": ["Erdem", "Ali", "Kutlu", "Uçan", "Vural", "Güler", "Alın", "Özdemir", "Yıldız"],
    "yas": [30, 34, 32, 33, 35, 33, 32, 40, 35],
    "cinsiyet": ["Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın"],
    "uyruk": ["Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk"],
    "sektor": ["İnşaat", "Teknoloji", "Diğer", "Teknoloji", "Diğer", "Teknoloji",
               "Muhasebe", "Teknoloji", "Muhasebe"],
    "tecrube": [3, 3, 3, 6, 3, 7, 3, 7, 6],
    "maas": [7000, 16000, 8000, 17000, 13000, 29000, 8000, 26000, 18000],
    "yipranma_payi": [0, 0.4, 0, 0, 0.3, 0, 0, 1.0, 0],
    "tesvik_primi": [0, 0, 1000, 0, 0, 1500, 0, 0, 2000]
}

df = pd.DataFrame(data)

# Gruplandırarak tecrube ve yeni maaş ortalamalarını hesaplama
gruplandirilmis_df = df.groupby("nesne_degeri").agg({"tecrube": "mean", "maas": "mean"})
print("\nTecrübe ve yeni maaş grup: ")
print(gruplandirilmis_df)

# Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
maas_15000_ustu = df[df["maas"] > 15000]
toplam_sayi = len(maas_15000_ustu)
print("\nMaaşı 15000 TL üzerinde olanların toplam sayısı:", toplam_sayi)

# Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
print("\nYeni Maaşa göre kücükten büyüğe sıralama: ")
siralama_df = df.sort_values(by="maas")
print(siralama_df)

# Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
print("\n Tecbrubesi 3 seneden fazla olan Beyaz Yakalılar: ")
tecrube_3_ustu = df[(df["nesne_degeri"] == "beyaz yaka") & (df["tecrube"] > 3)]
print(tecrube_3_ustu)