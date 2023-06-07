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

        