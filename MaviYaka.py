from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            tecrube = int(self.get_tecrube())
            maas = float(self.get_maas())
            yipranma_payi = float(self.__yipranma_payi)
            if tecrube < 2:
                return yipranma_payi * 10
            elif tecrube >= 2 and tecrube <= 4 and maas < 15000:
                return (maas * tecrube / 100) / 2 + (yipranma_payi * 10)
            elif tecrube > 4 and maas < 25000:
                return (maas * tecrube / 100) / 3 + (yipranma_payi * 10)
            else:
                return 0
        except ValueError:
            return 0

