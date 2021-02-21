#ÇALIŞMIYOR
#DÜZELTİLECEK

import random

kelime_data = ["Aba","Abaca","Abacan","Abaç","Abay","Abayhan","Abaza","Abbas", 'Abdal', 'Abdi','Abdullah','Abdurrahman',
'Abdülâlim', 'Abdülazim', 'Abdülaziz','Abdülbaki', 'Abdülbari', 'Abdülbasir','Abdülbasit', 'Abdülcabbar', 'Abdülcebbar',
'Abdülcelil','Abdülcemal',"Abdülcevat",'Abdülezel',"Abdülferit"]

sayac = 0

class Hangman:
    def __init__(self,kelime,gizli_kelime,harf,sayac):
        self.kelime = kelime
        self.gizli_kelime = gizli_kelime
        self.harf = harf
        self.sayac = sayac

    def kelime_sec():
        kelime = random.sample(kelime_data,1)[0]
        kelime = kelime.upper()
        return kelime

    def gizli_kelime_sec():
        gizli_kelime = ["_"] * len(kelime)
        return gizli_kelime

    def harf_ver(harf,kelime,gizli_kelime,sayac):
        for sayi in range(len(gizli_kelime)):
            for x in kelime:
                if harf == x:
                    gizli_kelime[sayi+sayac] = harf
            sayac += 1
        print(gizli_kelime)
        return sayac

print("Hangman Oyuna Hosgeldiniz")
kelime = Hangman.kelime_sec()
gizli_kelime = Hangman.gizli_kelime_sec()
print(type(gizli_kelime))
print(gizli_kelime)

for x in range(10):
    sayac1 = 0
    harf = input("Harf giriniz:").upper()
    Hangman.harf_ver(harf,kelime,gizli_kelime,sayac)
    sayac1 += 1