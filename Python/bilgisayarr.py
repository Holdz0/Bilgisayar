import time
import random
import os

pcdurum = 0


class bilgisayar():

    def __init__(self, pcdurum="Kapalı", internet="Bağlı Değil", googledurum="G_Kapalı",
                 programlar=[],ykprogramlar = ["google", "havalı yazı yazma", "sayı tahmin"] ):
        print("Bilgisayar oluşturuldu.")
        self.pcdurum = pcdurum
        self.internet = internet
        self.googledurum = googledurum
        self.programlar = programlar
        self.ykprogramlar = ykprogramlar

    def __str__(self):
        return ("Bilgisayar : {}\nİnternet Durumu : {}\nYüklü Programlar : {}".format(self.pcdurum, self.internet,
                                                                                      self.programlar))

    def pcac(self):
        if (self.pcdurum == "Kapalı"):

            print("Bilgisayar açılıyor. Lütfen bekleyin...")
            time.sleep(3)
            print("Bilgisayar Açıldı")
            self.pcdurum = "Açık"
            global pcdurum
            pcdurum = 1

        else:
            print("Bilgisayar zaten açık...")

    def pckapa(self):
        if (self.pcdurum == "Açık"):
            print("Bilgisayar Kapanıyor. Lütfen bekleyin...")
            time.sleep(3)
            print("Bilgisayar Kapandı")
            self.pcdurum = "Kapalı"

        else:
            print("Bilgisayar zaten kapalı...")

    def googleac(self):
        if ("Google" in self.programlar):

            if (self.googledurum == "G_Kapalı"):
                print("Google Açılıyor..")
                time.sleep(1)
                print("google açıldı")
                self.googledurum == "G_Açık"
                while True:
                    googleislem = input("""
Google'a Hoşgeldiniz

Araştırmak için konu seçiniz.

1-Muhammed Ulusoy aslında iplikçi mi ?
2-Seyit neden mal ?
3-Kızlarla nasıl konuşulur ?
4-Kimya quizleri nasıl fullenir ? 
5-Python mı daha iyi java mı ?
n - sonraki sayfa
q - Çıkış

                                            """)

                    if (googleislem == "1"):
                        os.system("cls")
                        print("""

İplikçi Nedim'in yer altı kaynakları ve şivesi Muhammed Ulusoyla
birebir örtüşmektedir. Daha fazla delile gerek olmadığı için evet.
Muhammed Ulusoy İplikçi Nedim'dir

                        """)

                    elif (googleislem == "2"):
                        os.system("cls")
                        print("""
                        Seyit'in Özellikleri

                        Mat : 7
                        Fizik -1
                        Hayatta kalma iç güdüsü : 1
                        Coğrafya : 3

                        Buradan anlaşılacağı üzere Seyit maldır.

                        """)

                    elif (googleislem == "3"):
                        os.system("cls")
                        print("Bilgisyar Mühendisleri bu kısıma erişemez.")
                        os.system("cls")
                    elif (googleislem == "4"):
                        os.system("cls")
                        print("""
Eğitim sürecinizde daha başarılı olmak ve konuları daha iyi anlamak için şu önerilere dikkat edebilirsiniz:

Düzenli Çalışma: Konuları düzenli bir şekilde çalışmak, öğrenmeyi güçlendirebilir.

Not Almak: Dersler sırasında not almak, öğrendiklerinizi gözden geçirmenize ve kavramanıza yardımcı olabilir.

Grup Çalışmaları: Konuları arkadaşlarınızla paylaşarak, birbirinize yardımcı olabilirsiniz.

Soru Çözme: Öğrendiğiniz konularla ilgili sorular çözmek, konuları daha iyi anlamanıza yardımcı olabilir.

Öğretme: Başkalarına öğretmek, öğrendiklerinizi pekiştirmenin etkili bir yoludur.

Her öğrencinin öğrenme tarzı farklıdır, 
bu nedenle sizin için en etkili yöntemleri bulmaya çalışın ve dürüst ve adil bir şekilde çalışarak başarı elde edin.
                        
                        
Tabi eğer hocanızın mutlu bir evliliği yoksa ne yaparsanız yapın 100 üzerinde 05 almak alın yazınız.
                        """)
                    elif (googleislem =="5"):
                        os.system("cls")
                        print("Java.(Bu program Python ile yazıldı...)")
                    elif (googleislem == "n"):
                        pass
                    elif (googleislem == "q"):
                        os.system("cls")
                        print("çıkış başarılı")
                        self.googledurum == "G_Kapalı"
                        break


                    else:
                        print("lütfen geçerli bir işlem giriniz")
        else:
            print("Google Yüklü Değil...")

    def programekle(self, i):
        self.programlar.append(i)

    def havaliyazi(self):
        while True: 
            hvgiris = input("Havalı Yazı Version 1\nHavalı Yazı version 2\nLütfen Sürüm Seçiniz (1/2) : ")
            if hvgiris == "1":

                h = ["a", "b", "c", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s",
     "ş", "t", "u", "ü", "v", "y", "z", "x", "w", " ", "ç", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
     "A", "B", "C", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S",
     "Ş", "T", "U", "Ü", "V", "Y", "Z"]

                ekran = ""
                sayac = 0
                anahtar = str(input("CÜMLE GİRİN : "))
                durum = False
                while True:

                    if durum:
                        break
                    for i in h:

                        print(ekran + i, end='', flush=True)
                        time.sleep(0.01)
                        print('\r' + '' * len(ekran + i), end='', flush=True)
                        try:

                            if i == anahtar[sayac]:
                                ekran += i
                                sayac += 1

                        except:
                            durum = True

                input("Çıkmak için bir tuşa basın")
                break

            elif (hvgiris == "2"):
                h = ["a", "b", "c", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s",
     "ş", "t", "u", "ü", "v", "y", "z", "x", "w", " ", "ç", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
     "A", "B", "C", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S",
     "Ş", "T", "U", "Ü", "V", "Y", "Z"]

                ekran = ""
                sayac = 0
                anahtar = str(input("CÜMLE GİRİN : "))
                durum = False
                while True:

                    if durum:
                        break
                    for i in h:

                        print(ekran+i)
                        time.sleep(0.01)
                        
                        try:

                            if i == anahtar[sayac]:
                                ekran += i
                                sayac += 1

                        except:
                            durum = True

                input("Çıkmak için bir tuşa basın")
                break
            else:
                print("Lütfen Geçerli Bir İşlem Giriniz...")


    def sayitahmin(self):
        print("""*****************************************


        sayı tahmin oyunu


        1 ile 40 arası bir sayı tahmin edin

        """)

        rastgelesayi = random.randint(1, 40)
        tahminhakki = 5

        while True:
            print("tahmin hakkı : ", tahminhakki)
            tahmin = int(input("Tahmininiz : "))

            if (tahmin > 40):
                print("lütfen adam gibi bir sayı girin")


            elif (tahmin < rastgelesayi):
                print("Bilgiler analiz ediliyor...")
                time.sleep(1)
                print("Daha yüksek bir sayı tahmin edin")

                tahminhakki -= 1
            elif (tahmin > rastgelesayi):
                print("Bilgiler analiz ediliyor...")
                time.sleep(1)
                print("Daha düşük bir sayı tahmin edin")

                tahminhakki -= 1

            else:
                print("Bilgiler analiz ediliyor...")
                time.sleep(1)
                print("AFFERİM LAN DOĞRU CEVAP")
                time.sleep(10)
                break
            if (tahminhakki == 0):
                print("Tahmin hakkınız bitti")
                print("Sayınız :", rastgelesayi)
                time.sleep(10)
                break

    def programuı(self):
        while True:
            pcislem = input("""Yapmak istediğiniz işlemi seçiniz.

            1-Program Çalıştır

            2-Program Yükle

            3-Program Kaldır

            4-Çıkış

          """)
            if (pcislem == "1"):
                print(self.programlar)
                prginput = input("Çalıştırmak istediğiniz programı yazınız : ")
                prginput = prginput.lower()
                for prginput in self.programlar:
                    if prginput == "google":
                        os.system("cls")
                        efeninpc.googleac()
                    elif prginput == "havalı yazı yazma":
                        os.system("cls")
                        efeninpc.havaliyazi()
                    elif prginput == "sayı tahmin":
                        os.system("cls")
                        efeninpc.sayitahmin()
                    else:
                        print("lütfen adam gibi bir değer girin")

            elif (pcislem == "2"):
                print(self.ykprogramlar)
                eklenecekprgrm = input("Lütfen yüklenecek programların ismini araya ',' koyarak yazınız. : ")
                programlistesi = eklenecekprgrm.split(",")

                for i in programlistesi:
                    efeninpc.programekle(i)
                    self.ykprogramlar.remove(i)

                print("programlar eklendi")

            elif (pcislem == "3"):
                prgmrsil = input("Lütfen kaldırmak istediğiniz programı yazınız : ")
                
                if (prgmrsil in self.programlar):
                    self.programlar.remove(prgmrsil)
                    print("İşlem Başarılı.")
                    self.ykprogramlar.append(prgmrsil)
                else:
                    print("Böyle bir program bulunmuyor.")
            elif (pcislem == "4"):
                print("Çıkış Yaplıyor")
                time.sleep(1)
                print("""
**************************************************

Hoşgeldiniz...

1-Bilgisayarı Aç

2-Bilgisayarı Kapa

3-Programlar

********************************************************     
                """)
                break


efeninpc = bilgisayar()
print("""
    **************************************************

    Hoşgeldiniz...

    1-Bilgisayarı Aç

    2-Bilgisayarı Kapa

    3-Programlar

********************************************************     
""")

while True:

    islem = input("İşlem Seçiniz : ")
    if (islem == "1"):
        os.system("cls")
        efeninpc.pcac()
    elif (islem == "2"):
        os.system("cls")
        efeninpc.pckapa()
        cikisonay = input("Uygulamadan Çıkmak İster misiniz ? (y/n)\n")
        if cikisonay == "y":
            break
        else:
            print("""
    **************************************************

    Hoşgeldiniz...

    1-Bilgisayarı Aç

    2-Bilgisayarı Kapa

    3-Programlar

********************************************************     
""")
    elif (islem == "3"):
        if (pcdurum == 1):
            os.system("cls")

            efeninpc.programuı()
        else:
            print("lütfen ilk önce bilgisayarı açınız")
            print(pcdurum)
    else:
        print("Lütfen geçerli bir işlem giriniz...")
        time.sleep(3)








