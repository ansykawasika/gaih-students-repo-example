sinif = []
puanlar = []
sinavlar = ["vize","final","odev"]
info = {}
info_average = {}

def Ogrenci_Kayit():
    for i in range(n):
        ad = input(f"{i+1}. öğrencininin adini giriniz: ").title()
        soyad = input (f"{i+1}. öğrencinin soyadini giriniz: ").upper()
        ogrenci = ad + " " + soyad 
        sinif.append(ogrenci)

def Puan_Ver():
    sayac = 0
    for ogrenci in sinif:
        for j in sinavlar:
            while 1:
                try:
                    puan = int(input(f"{ogrenci} in {j} notunu giriniz: "))
                    break
                except ValueError:
                    print("Yanlış girdiniz.")
            puanlar.append(puan)
        data = {ogrenci : puanlar[sayac:sayac+3]}
        info.update(data)
        sayac += 3

def Ortalama_hesapla():
    for i in info:
        summ = 0
        for j in info.get(i):
            summ = summ + j
        average = summ / 3
        data = {i : average}
        info_average.update(data)

def Tebrik(info,info_average):
    info_average = sorted(info_average.items(), key = lambda kv:(kv[1], kv[0]))
    sayac = 0
    for i in info.values():
        print(f"{list(info.keys())[sayac]}'ün vize notu {i[0]},final notu {i[1]}, ödev notu ise {i[2]}")
        sayac += 1
    print("***SINIF ORTALAMA SIRALAMASI***")
    sayac = 1
    for i in info_average[::-1]:
        print(f"{sayac}. {i[0]}  ortalama:{round(i[1],2)}")
        sayac += 1
    print(f"TEBRİKLERRRR EN YÜKSEK ORTALAMAYA SAHİP ÖGRENCİ {info_average[-1][0]}. ")
       

n = int(input("Sınıfınız kaç kişi: "))
Ogrenci_Kayit()
Puan_Ver()
Ortalama_hesapla()
Tebrik(info,info_average)