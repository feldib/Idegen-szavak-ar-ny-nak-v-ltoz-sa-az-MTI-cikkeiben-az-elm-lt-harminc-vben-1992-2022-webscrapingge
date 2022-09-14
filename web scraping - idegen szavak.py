import requests as requests
from requests import get
from bs4 import BeautifulSoup

#ide fogjuk szétszedni
class Idegen_szavak:
    def __init__(self):
        self._SZÓ=""
        self._JELENTÉS=""
        self._EREDETE=""
        self._FORRÁS=""
    
    @property
    def Szó(self):
        return self._SZÓ
    @Szó.setter
    def Szó(self, szó):
        self._SZÓ=szó
        
    @property
    def Jelentés(self):
        return self._JELENTÉS
    @Jelentés.setter
    def Jelentés(self, jelentés):
        self._JELENTÉS=jelentés
        
    @property
    def Eredete(self):
        return self._EREDETE
    @Eredete.setter
    def Eredete(self, eredete):
        self._EREDETE=eredete

    @property
    def Forrás(self):
        return self._FORRÁS
    @Forrás.setter
    def Forrás(self, forrás):
        self._FORRÁS=forrás
        
    def Kiír(self):
        print("szó:",self._SZÓ)
        print("jenetés:",self._JELENTÉS)
        print("eredete:",self._EREDETE)
        print("forrás:",self._FORRÁS)
        
#urlok összegyűjtése (majd írd át hogy ne mentse tömbbe!)
url = "https://idegen-szavak.hu/szavak/abc_sorrendben/"
urlok = [url]
i=5
while i<=10090:
    urlok.append(url+str(i))
    i+=5

#mentsük ki a tanálatokat(class="item")
items=0
kifile = open("idegen szavak.csv", "wt", encoding="utf-16", newline='')
ch = "|"
kifile.write("Szó"+ch+"Jelentés"+ch+"Eredete"+ch+"Forrás"+"\n")
for j in urlok:
    results=requests.get(j)
    soup=BeautifulSoup(results.text, "html.parser")
    bejegyzes = soup.find_all('div', class_='item')
    for i in bejegyzes:
        idegen_szó = Idegen_szavak()
        idegen_szó.Szó = i.h1.a.text.strip()
        idegen_szó.Jelentés = i.p.text.replace("\r", " ").replace("\n"," ").strip()
        eredet_és_forrás=i.find('div', class_='meta').find_all('p')
        idegen_szó.Eredete = str(eredet_és_forrás[0]).split(">")[3].split("<")[0].strip()
        idegen_szó.Forrás = str(eredet_és_forrás[1]).split(">")[3].split("<")[0].strip()
        idegen_szó.Kiír()
        kifile.write(idegen_szó.Szó +ch+ idegen_szó.Jelentés +ch+ idegen_szó.Eredete +ch+ idegen_szó.Forrás+"\n")
        items+=1
        print(items, "darab beolvasva")
kifile.close()