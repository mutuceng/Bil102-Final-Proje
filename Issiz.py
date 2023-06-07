from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = tecrube_dict
    def get_tecrube_dict(self):
        return self.__tecrube_dict
    def set_tecrube_dict(self, tecrube_dict):
        self.__tecrube_dict = tecrube_dict

    def statu_bul(self):
        try:
            statuler = {
                "mavi yaka": 0,
                "beyaz yaka": 0,
                "yönetici": 0
            }
            for statu, yil in self.__tecrube_dict.items():
                if statu == "mavi yaka":
                    statuler[statu] += yil * 0.2
                elif statu == "beyaz yaka":
                    statuler[statu] += yil * 0.35
                elif statu == "yönetici":
                    statuler[statu] += yil * 0.45
            return max(statuler, key=statuler.get)
        except ValueError:
            return None

    def __str__(self):
        try:
            en_uygun_statu = self.statu_bul()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {en_uygun_statu}"
        except ValueError:
            return "Geçersiz değerler!"