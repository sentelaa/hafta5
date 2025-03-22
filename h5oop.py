class hesap ():
    def _init_(self, say1, say2):
        self.say1 = say1
        self.say2 = say2

    def carp(self):
        sonuc = self.say1 * self.say2
        return sonuc

    def bol(self):
        sonuc = self.say1 / self.say2
        return sonuc

    def top(self):
        sonuc = self.say1 + self.say2
        return sonuc

    def cıkar(self):
        sonuc = self.say1 - self.say2
        return sonuc

    def yazdır(self):
        toplam = self.top()
        carpma = self.carp()
        print("toplama sonucu", toplam)
        print("carpma sonucu", carpma)
