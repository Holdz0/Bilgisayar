import time
import random
import os
import sqlite3
import webbrowser

pcdurum = 0
def karsilamapc():
    print("""
********************************************************

    Hoşgeldiniz...

    1-Bilgisayarı Aç

    2-Bilgisayarı Kapa

    3-Programlar

********************************************************     
""")
def sqlveri():
    con = sqlite3.connect("kullanıcılar.db")
    idlist = []
    cursor = con.cursor()

    def tablo_olustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS kullanıcılar (İsim TEXT, Görev TEXT, Şifre TEXT, Kullanıcı_ID TEXT)")
        con.commit()
    tablo_olustur()
    def deger_ekle(isim,gorev,sifre,rastgelesayi):
        cursor.execute("INSERT INTO kullanıcılar VALUES(?,?,?,?)", (isim, gorev,sifre, rastgelesayi))
        con.commit()
    def verileri_al():
        cursor.execute("Select * From kullanıcılar") 
        data = cursor.fetchall() 
        print("Kitaplık Tablosunun bilgileri.....")
        for i in data:
            print(i)

    def rastgeleolustur():
        rsg1 = random.randint(0, 9)
        rsg2 = random.randint(0, 9)
        rsg3 = random.randint(0, 9)
        rsg4 = random.randint(0, 9)
        rsg1 = str(rsg1)
        rsg2 = str(rsg2)
        rsg3 = str(rsg3)
        rsg4 = str(rsg4)

        tplm = rsg1  + rsg2 + rsg3 + rsg4
        return tplm

    def veri_sil():
        pass

    while True:
        komut = input("""Yapmak istediğiniz işlem :
        
        1 - Verileri Görüntüle
        
        2 - Yeni Veri Ekle
        
        3 - Çıkış
            
        """)
        if (komut == "1"):
            verileri_al()
        elif (komut == "2"):
            isim = input("lütfen İsim Girin : ")
            gorev = input("Lütfen Görev Girin : ")
            sifre = input("Lütfen Şifre Girin : ")
            rastgelesayi = rastgeleolustur()
            while True: 
                if rastgelesayi in idlist:
                    print("Bu sayı zaten listede var. Yeni bir sayı üretiyorum...")
                    rastgelesayi = rastgeleolustur()
                else:
                    print("Kaydedildi")
                    idlist.append(rastgelesayi)
                    deger_ekle(isim,gorev,sifre,rastgelesayi)
                    break

        elif (komut == "3"):
            kullanicigirdi()
            break
        else:
            print("adam gibi bişe gir")
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
            time.sleep(1.5)
            print("Bilgisayar Açıldı")
            self.pcdurum = "Açık"
            global pcdurum
            pcdurum = 1

        else:
            print("Bilgisayar zaten açık...")

    def pckapa(self):
        if (self.pcdurum == "Açık"):
            print("Bilgisayar Kapanıyor. Lütfen bekleyin...")
            time.sleep(1.5)
            print("Bilgisayar Kapandı")
            self.pcdurum = "Kapalı"

        else:
            print("Bilgisayar zaten kapalı...")

    def googleac(self):
        if ("google" in self.programlar):

            if (self.googledurum == "G_Kapalı"):
                print("Google Açılıyor..")
                time.sleep(1)
                print("google açıldı")
                self.googledurum == "G_Açık"
                while True:
                    googleislem = input("""
Google'a Hoşgeldiniz

Araştırmak için konu seçiniz.

1 - Muhammed Ulusoy aslında iplikçi mi ?
2 - Seyit neden mal ?
3 - Kızlarla nasıl konuşulur ?
4 - Kimya quizleri nasıl fullenir ? 
5 - Python mı daha iyi java mı ?
r - The Google
q - Çıkış

işlem : """)

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
                    elif (googleislem == "r"):
                        url = f'https://www.google.com/search?q='
                        url2 = input('ne araştırmak istersiniz : ')
                        webbrowser.open(url+url2)
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
                for i in self.programlar:
                    if prginput == "google" and i == "google":
                        os.system("cls")
                        efeninpc.googleac()
                        break
                    if prginput == "havalı yazı yazma" and i == "havalı yazı yazma":
                        os.system("cls")
                        efeninpc.havaliyazi()
                        break
                    if prginput == "sayı tahmin" and i == "sayı tahmin":
                        os.system("cls")
                        efeninpc.sayitahmin()
                        break
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
                karsilamapc()
                break


efeninpc = bilgisayar()

def kullanicigirdi():
    print("""
    **************************************

    Hoşgeldiniz Bilgisayar programını kullanmak için giriş yapın:

    1- Giriş Yap
    2- Kayıt Ol
    3- Admin Giriş
    4- Çıkış

    ***************************************
    """)

    kullanici_adi = ["admin","1"]  #sorgulayıcısı a
    kullanici_sifre = ["0000","1"] # sorgulayıcı b
    a = len(kullanici_adi)
    b = len(kullanici_sifre)

    demetsorgusira = 0

    yetkiizin = False

    class yetkili():

        def __init__(self, isim, soyisim, yetki_duzeyi, yas):
            self.isim = isim
            self.soyisim = soyisim
            self.yetki_duzeyi = yetki_duzeyi
            self.yas = yas

        def bilgilerigoster(self):
            print("""

            İsim = {}  

            Soy isim = {}  

            Yetki Düzeyi = {}

            Yaş = {}
                            """.format(self.isim, self.soyisim, self.yetki_duzeyi, self.yas))
        def saldiribaslat(self):
            print("saldırı başlatılıyor...")
            saldiribaslat = True

        def yetkizin(self):
            print("yetki verildi")
            yetkiizin = True

        def adminpanell(self):

            sqlveri()
            
    admin = yetkili("Taha Efe","Tuncer","üst Düzey",18)



    ilkislemsorgu = True


    while ilkislemsorgu:
        girdi = input("işlem giriniz : ")

        if girdi == "1":
            girdi_kullanici_adi = str(input("Kullanıcı adını giriniz : "))
            girdi_kullanici_sifre = str(input("Şifre giriniz : "))

            for demetsorgusira in range(len(kullanici_adi)):
                if girdi_kullanici_adi != kullanici_adi[demetsorgusira] or girdi_kullanici_sifre != kullanici_sifre[demetsorgusira]:
                    demetsorgusira += 1


                elif girdi_kullanici_adi == kullanici_adi[demetsorgusira] and girdi_kullanici_sifre == kullanici_sifre[demetsorgusira]:
                    karsilamapc()
                    karsilamainput()
                    break

            else:
                print("kullanıcı adı veya şifre yanlış")

        elif girdi == "2":
            kayit_kullanici = str(input("Yeni kullanıcı adını giriniz : "))
            kayit_sifre = str(input("Yeni şifre giriniz : "))
            while True:
                if kayit_kullanici in kullanici_adi:
                    kayit_kullanici = str(input("Bu kullanıcı adı zaten kayıtlı...\nLütfen Başka bir kullanıcı adi giriniz : \n"))
                else:   

                    kullanici_adi.append(kayit_kullanici)
                    kullanici_sifre.append(kayit_sifre)
                    print("Başarıyla kaydedildi")
                    break

        elif girdi == "3":
            admin_kullanici = input("Kullanıcı adı giriniz : ")
            admin_sifre = input("şifre giriniz : ")

            if admin_kullanici == "admin" and admin_sifre == "0000":
                print("giriş başarılı")
                ilkislemsorgu = False
                admin.adminpanell()
        elif girdi == "4":
            break
        else:
            print("adam gibi işlem gir la")
            continue
def karsilamainput():

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
                kullanicigirdi()
                break
            else:
                karsilamapc()
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
kullanicigirdi()