from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.__sektorKontrol(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

    def __sektorKontrol(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor.lower() in sektorler:
            return sektor.lower()
        else:
            raise ValueError(f"Geçersiz sektor: {sektor}. Geçerli sektorler: {sektorler}")

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.__sektorKontrol(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            tecrube = int(self.__tecrube)
            maas = float(self.__maas)
            zam_orani = maas % tecrube

            if tecrube < 2 or maas >= 25000:
                return 0
            elif tecrube >= 2 and tecrube <= 4 and maas < 15000:
                return maas * (zam_orani / 100)
            elif tecrube > 4 and maas < 25000:
                return maas * (zam_orani / 200)
            else:
                return 0
        except ValueError:
            return 0

    def __str__(self):
        try:
            yeni_maas = float(self.__maas) + self.zam_hakki()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} yıl\nYeni Maaş: {yeni_maas:.2f}"
        except ValueError:
            return "Geçersiz değerler!"