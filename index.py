"""
Nihat Furkan Çiftçi
21763139
Final Ödevi
"""
from tkinter import *


class kitaplık:
    def __init__(self,anaSayfa):
        global ısbn, ısbnalanı
        global kitap, kitapadı
        global yazar, yazaradı
        global yıl, yayınyılı



        self.anaSayfa = anaSayfa
        anaSayfa.title("KİTAP ARAMA SİHİRBAZI")



        anaSayfa.configure(background="white")
        anaSayfa.geometry("650x650+250+0")



        ısbn = ["9752430297", "9752633711", "9752430563","6051140957","6055411251"]
        kitapadı = ["gazi mustafa kemal atatürk","osmanlıyı yeniden keşfetmek","osmanlı imparatorluğu","abdülhamidin kurtlarla dansı","atatürk ve demokratik türkiye"]
        yazaradı = ["ilber ortaylı", "ilber ortaylı","halil inalcık","mustafa armağan","halil inalcık"]
        yayınyılı = ["2018", "2009", "1973", "2006","2000"]



        giriş = Label(anaSayfa, text="Kitap Arama Sihirbazına Hoşgeldiniz\n Lütfen arama yapmak istediğniz kutucuğa uygun bilgileri giriniz", bg="white", fg="black",font=("arial",12)).grid(padx=80)



        kitapları_listele = Button(anaSayfa, text="Kitap Listelesi", bg="red", fg="white",font="bold", command=self.kitaplari_listele)
        kitapları_listele.grid( row="1")



        arama = Label(anaSayfa, text="Aramak istediğiniz kitabın ISBN numarasını giriniz:", bg="white", fg="black", font=("times new roman", 12)).grid(row=3,sticky=W )
        ısbnalanı = Entry(width=30)
        ısbnalanı.grid(row=3,sticky=E)
        buton = Button(anaSayfa,text="BUL", bg="white", fg="black", font=("calibri", 10), command=self.giris0).grid(row=3, column=3)


        arama = Label(anaSayfa, text="Aramak istediğiniz kitabın adını giriniz:", bg="white", fg="black",font=("times new roman", 12)).grid(row=4, sticky=W)
        kitap = Entry(width=30)
        kitap.grid(row=4,sticky=E)
        buton = Button(anaSayfa, text="BUL", bg="white", fg="black", font=("calibri", 10), command=self.giris1).grid(row=4, column=3)


        arama= Label(anaSayfa, text="Aramak istediğiniz kitabın yazarını giriniz:", bg="white", fg="black",font=("times new roman", 12)).grid(row=5, sticky=W)
        yazar = Entry(width=30)
        yazar.grid(row=5, sticky=E)
        buton = Button(anaSayfa, text="BUL", bg="white", fg="black", font=("calibri", 10),command=self.giris2).grid(row=5,column=3)


        arama = Label(anaSayfa, text="Aramak istediğiniz kitabın yayın yılını giriniz:", bg="white", fg="black",font=("times new roman", 12)).grid(row=6, sticky=W)
        yıl = Entry(width=30)
        yıl.grid(row=6, sticky=E)
        buton = Button(anaSayfa, text="BUL", bg="white", fg="black", font=("calibri", 10),command=self.giris3).grid(row=6, column=3)
        self.kitap_ekle = Button(anaSayfa, text="Kitap Ekle", bg="black", fg="yellow", font="bold",
        command=self.kitap_ekle)
        self.kitap_ekle.grid()

    def kitap_ekle(self):
        global kitap_adi, yazar_adi, tur, isbn, yy, pencere1
        pencere1 = Tk()

        baslik1 = pencere1.title("Kitap Kayıt Sihirbazı")
        pencere1.configure(background="white")

        kitap_adi = Entry(pencere1)
        kitap_adi.grid(row=3)
        yazar_adi = Entry(pencere1)
        yazar_adi.grid(row=4)
        isbn = Entry(pencere1)
        isbn.grid(row=6)
        yy = Entry(pencere1)
        yy.grid(row=7)
        self.kaydet = Button(pencere1, text="KAYIT", command=self.kitap_kaydet, fg="white", bg="red")
        self.kaydet.grid(row=8)

        self.cıkıs = Button(pencere1, text="ÇIKIŞ", command=pencere1.destroy, fg="white", bg="red")
        self.cıkıs.grid(column=3, row=8)

        Label(pencere1, bg="white", fg="black", text='ISBN :').grid(column=2, row=3)
        Label(pencere1, bg="white", fg="black", text='Kitap Adı: ').grid(column=2, row=4)
        Label(pencere1, bg="white", fg="black", text='Yazar Adı: ').grid(column=2, row=5)
        Label(pencere1, bg="white", fg="black", text='Yayın Yılı :').grid(column=2, row=6)

    def kitap_kaydet(self):
        kayit_sis = str(( kitap_adi.get() + "/" + yazar_adi.get() + "/"  + isbn.get() + "/" + yy.get()) + "\n")
        dosya = open("katalog.txt", "a")
        for i in kayit_sis:
            dosya.write(i)
        dosya.close()
        command = pencere1.destroy()



        self.cikis = Button(anaSayfa, text="ÇIKIŞ", command=exit, fg="white", bg="red",)
        self.cikis.grid(row=7, column=7)


    def giris3(self):
        yılı = yıl.get()

        if yılı == yayınyılı[0]:
            bir = Label(root,text="ISBN: 9752430297 \n KİTAP ADI: Gazi Mustafa Kemal Atatürk \n YAZAR ADI: İlber Ortaylı \n TÜR: Biyografi \n YAYIN YILI: 2018  ", bg="lightblue",fg="black" , font=("Times New Roman",12)).grid()

        elif yılı == yayınyılı[1]:
            iki = Label(root,text="ISBN: 9752633711 \n KİTAP ADI: Osmanlıyı Yeniden Keşfetmek \n YAZAR ADI: İlber Ortaylı \n TÜR: Tarih \n YAYIN YILI: 2009  ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()


        elif yılı == yayınyılı[2]:
            üç = Label(root,text="ISBN: 9752430563 \n KİTAP ADI: Osmanlı İmparatorluğu \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 1973 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif yılı == yayınyılı[3]:
            dört = Label(root,text="ISBN: 6051140957 \n KİTAP ADI: Abdulhamid'in Kurtlarla Dansı \n YAZAR ADI: Mustafa Armağan \n TÜR: Tarih \n YAYIN YILI: 2006 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif yılı == yayınyılı[4]:
            beş = Label(root,text="ISBN: 6055411251 \n KİTAP ADI: Atatürk ve Demokratik Türkiye \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 2000 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()
        else:
            yok = Label(root,text="Aradığınız kitap kütüphanemizde bulunmamaktadır..." , bg="lightblue",fg="black", font=("Times New Roman", 12)).grid()




    def giris2(self):
        yaz = yazar.get()

        if yaz == yazaradı[0]:
            bir = Label(root,text="ISBN: 9752430297 \n KİTAP ADI: Gazi Mustafa Kemal Atatürk \n YAZAR ADI: İlber Ortaylı \n TÜR: Biyografi \n YAYIN YILI: 2018  ", bg="lightblue",fg="black" , font=("Times New Roman",12)).grid()

        elif yaz ==yazaradı[1]:
            iki = Label(root,text="ISBN: 9752633711 \n KİTAP ADI: Osmanlıyı Yeniden Keşfetmek \n YAZAR ADI: İlber Ortaylı \n TÜR: Tarih \n YAYIN YILI: 2009  ", bg="lightblue",fg="black", font=("Times New Roman", 12)).grid()

        elif yaz == yazaradı[2]:
            üç = Label(root,text="ISBN: 9752430563 \n KİTAP ADI: Osmanlı İmparatorluğu \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 1973 ", fg="black", font=("Times New Roman", 12)).grid()

        elif yaz == yazaradı[3]:
            dört = Label(root,text="ISBN: 6051140957 \n KİTAP ADI: Abdulhamid'in Kurtlarla Dansı \n YAZAR ADI: Mustafa Armağan \n TÜR: Tarih \n YAYIN YILI: 2006 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif yaz == yazaradı[4]:
            beş = Label(root,text="ISBN: 6055411251 \n KİTAP ADI: Atatürk ve Demokratik Türkiye \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 2000 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()
        else :
            yok = Label(root,text="Aradığınız kitap kütüphanemizde bulunmamaktadır..." , bg="lightblue",fg="black", font=("Times New Roman", 12)).grid()




    def giris1(self):
        adı = kitap.get()

        if adı == kitapadı[0]:

            bir = Label(root,text="ISBN: 9752430297 \n KİTAP ADI: Gazi Mustafa Kemal Atatürk \n YAZAR ADI: İlber Ortaylı \n TÜR: Biyografi \n YAYIN YILI: 2018  ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif adı == kitapadı[1]:
            iki = Label(root,text="ISBN: 9752633711 \n KİTAP ADI: Osmanlıyı Yeniden Keşfetmek \n YAZAR ADI: İlber Ortaylı \n TÜR: Tarih \n YAYIN YILI: 2009  ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif adı == kitapadı[2]:
            üç = Label(root, text="ISBN: 9752430563 \n KİTAP ADI: Osmanlı İmparatorluğu \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 1973 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif adı == kitapadı[3]:
            dört = Label(root,text="ISBN: 6051140957 \n KİTAP ADI: Abdulhamid'in Kurtlarla Dansı \n YAZAR ADI: Mustafa Armağan \n TÜR: Tarih \n YAYIN YILI: 2006 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif adı == kitapadı[4]:
            beş = Label(root,text="ISBN: 6055411251 \n KİTAP ADI: Atatürk ve Demokratik Türkiye \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 2000 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()
        else:
            yok = Label(root, text="Aradığınız kitap kütüphanemizde bulunmamaktadır...", bg="lightblue", fg="black",font=("Times New Roman", 12)).grid()



    def giris0(self):
        ısbnn = ısbnalanı.get()

        if ısbnn == ısbn[0]:

            bir = Label(root,text="ISBN: 9752430297 \n KİTAP ADI: Gazi Mustafa Kemal Atatürk \n YAZAR ADI: İlber Ortaylı \n TÜR: Biyografi \n YAYIN YILI: 2018  ", bg="lightblue",fg="black" , font=("Times New Roman",12)).grid()

        elif ısbnn == ısbn[1]:
            iki = Label(root,text="ISBN: 9752633711 \n KİTAP ADI: Osmanlıyı Yeniden Keşfetmek \n YAZAR ADI: İlber Ortaylı \n TÜR: Tarih \n YAYIN YILI: 2009  ", bg="lightblue",fg="black", font=("Times New Roman", 12)).grid()

        elif ısbnn == ısbn[2]:
            üç = Label(root,text="ISBN: 9752430563 \n KİTAP ADI: Osmanlı İmparatorluğu \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 1973 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif ısbnn == ısbn[3]:
            dört = Label(root,text="ISBN: 6051140957 \n KİTAP ADI: Abdulhamid'in Kurtlarla Dansı \n YAZAR ADI: Mustafa Armağan \n TÜR: Tarih \n YAYIN YILI: 2006 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()

        elif ısbnn == ısbn[4]:
            beş = Label(root,text="ISBN: 6055411251 \n KİTAP ADI: Atatürk ve Demokratik Türkiye \n YAZAR ADI: Halil İnalcık \n TÜR: Tarih \n YAYIN YILI: 2000 ",bg="lightblue", fg="black", font=("Times New Roman", 12)).grid()
        else:
            yok = Label(root,text="Aradığınız kitap kütüphanemizde bulunmamaktadır..." , bg="lightblue",fg="black", font=("Times New Roman", 12)).grid()

    def kitaplari_listele(self):
            pencerex= Tk()
            baslik2 = pencerex.title("Kayıtlı Kitaplar")
            pencerex.configure(background="black")
            file = open("katalog.txt")
            data = file.read()
            file.close()

            kitap_liste = Label(pencerex, text=data,fg="yellow", bg="black")
            kitap_liste.pack()

root = Tk()
yeniPencere = kitaplık(root)
root.mainloop()

