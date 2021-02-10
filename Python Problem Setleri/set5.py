class Okul:
    def __init__(self, adi, turu, dersozellikleri, kurulusyili, dersliksayisi, ogretmensayisi, mevcut):
        self.adi = adi
        self.turu = turu
        self.dersozellikleri = dersozellikleri
        self.kurulusyili = kurulusyili
        self.dersliksayisi = dersliksayisi
        self.ogretmensayisi = ogretmensayisi
        self.mevcut = mevcut


Okul_1 = Okul("Halit", "İlkokul", "Resmi Müfredat", 1989, 20, 30, 560)
Okul_2 = Okul("Rehu", "Lise", "ResmiMüfredat", 1999, 30, 40,
              750)
Okul_3 = Okul("Fırat", "Üniversite","Resmi-Seçmeli Müfredat, Serbest Etkinlikler", 1980, 250, 190, 1200)

Okullar = [Okul_1, Okul_2, Okul_3]

for okul in Okullar:
    print(okul.adi, okul.turu, okul.dersozellikleri, okul.kurulusyili, okul.dersliksayisi,
          okul.ogretmensayisi, okul.mevcut)