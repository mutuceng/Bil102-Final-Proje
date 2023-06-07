from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            tecrube = int(self.get_tecrube())
            maas = float(self.get_maas())
            tesvik_primi = float(self.__tesvik_primi)
            if tecrube < 2:
                return tesvik_primi
            elif tecrube >= 2 and tecrube <= 4 and maas < 15000:
                return (maas * tecrube / 100) * 5 + tesvik_primi
            elif tecrube > 4 and maas < 25000:
                return (maas * tecrube / 100) * 4 + tesvik_primi
            else:
                return 0
        except ValueError:
            return 0

    def __str__(self):
        try:
            yeni_maas = float(self.get_maas()) + self.zam_hakki()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} yıl\nYeni Maaş: {yeni_maas:.2f}"
        except ValueError:
            return "Geçersiz değerler!"
