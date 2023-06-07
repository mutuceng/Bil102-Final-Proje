from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.__sektorKontrol(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

