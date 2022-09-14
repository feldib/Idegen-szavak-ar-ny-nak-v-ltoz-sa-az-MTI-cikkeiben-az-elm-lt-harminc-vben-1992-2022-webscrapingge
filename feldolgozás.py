import time
import requests as requests
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_read_close_articles():
    for n in range(18):
        wait = WebDriverWait(driver, 120)
        címclass='.lbCim'
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, címclass)))
        cím = driver.find_element(By.CSS_SELECTOR, címclass).get_attribute('innerText')
        if ("Labdarúgó NB I " not in cím.split('-') and cím!="TOTÓ-eredmények" and cím!="A KENÓ nyerőszámai" and cím not in címek):
            címek.append(cím)
            time.sleep(2)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.lbDatum')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".lbLd")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".lbHir")))
            dátum = driver.find_element(By.CSS_SELECTOR, '.lbDatum').get_attribute('innerText')
            szoveg = ' '.join([
                cím,
                driver.find_element(By.CSS_SELECTOR, ".lbLd").get_attribute('innerText'),
                driver.find_element(By.CSS_SELECTOR, ".lbHir").get_attribute('innerText')
                ])
            #ide kéne jöjjön az adatok classba mentése, majd kiirasa
            article = Item()
            article.Cím = cím
            article.Dátum = dátum
            print(cím)
            print(dátum)
            #ide jön az elemzés(hány idegen szó, és milyen eredetűek)
            feldolgozas(szoveg, article)
            #itt kéne hogy jöjjön a kiiras fájlba
            kifile.write(article.Kiír())
        else:
            print("Átugorva!!")
        time.sleep(2)
        következő=driver.find_element(By.XPATH, "//*[@id=\"ctl00_SearchPlaceHolder_onePdfControl1_NextResultLink\"]")
        következő.click()
        print("open_read_close_articles loopja lefutott", n+1 ,'-szer')
    print("open_read_close_articles program lefutott.")
    driver.find_element(By.ID, 'ctl00_SearchPlaceHolder_onePdfControl1_hlBack').click()
    time.sleep(2)

# def lapozz(sorszam):
#     wait = WebDriverWait(driver, 30)
#     következő='//*[@id=\"ctl00_SearchPlaceHolder_PDFsearchList1_dpgNewsList\"]/a['+str(sorszam)+']'
#     print(következő)
#     wait.until(EC.presence_of_element_located((By.XPATH, következő)))
#     driver.find_element(By.XPATH, következő).click()
#     print("Sikeresen lapozott")

def feldolgozas(szoveg, article):
    szavak = szoveg.split(' ')
    article.Szavak_száma = len(szavak)
    for i in range(len(szavak)):
        befile = open("releváns szavak(adattisztítás után).csv", "rt")
        befile.readline()
        sor=befile.readline()
        not_found = True
        while not_found and sor!="":
            szó = sor.split(";")[0]# a "szó" a szótárban lévő szavakra vonatkozik
            nyelv = sor.split(";")[1].replace('\n','').replace('\r','')
            if i>=3 and len(szó.split(" "))==3:
                if szó in ' '.join([szavak[i-2], szavak[i-1], szavak[i-2]]):
                    nyelv_növel(nyelv, article)
                    not_found=False
            elif i>=2 and len(szó.split(" "))==2:
                if szó in ' '.join([szavak[i-1], szavak[i-2]]):
                    nyelv_növel(nyelv, article)
                    not_found=False
            else:
                if szó in szavak[i]: #emiatt akkor is találatot ad, ha ragozott szóként szerepelt a szó a cikkben
                    nyelv_növel(nyelv, article)
                    not_found=False
            sor=befile.readline()
        befile.close()

        
def nyelv_növel(nyelv, article):
    if len(nyelv.split('+'))==2:
        article.Idegen_szavak = nyelv.split('+')[0]
        article.Idegen_szavak = nyelv.split('+')[1]
        article.Idegen_szavak_száma = 2
    elif len(nyelv.split('-'))==2:
        article.Idegen_szavak = nyelv.split('-')[0]
        article.Idegen_szavak = nyelv.split('-')[1]
        article.Idegen_szavak_száma = 2
    elif len(nyelv.split(', '))==2:
        article.Idegen_szavak = nyelv.split(', ')[0]
        article.Idegen_szavak = nyelv.split(', ')[1]
        article.Idegen_szavak_száma = 2
    else:
        article.Idegen_szavak = nyelv
        article.Idegen_szavak_száma = 1

class Item:
    def __init__(self):
        self.__Cím = ""
        self.__Szavak_száma = 0
        self.__Dátum = ""
        self.__Idegen_szavak_száma = 0
        self.__Idegen_szavak = {
            'latin' : 0,
            'görög' : 0,
            'angol' : 0,
            'francia' : 0,
            'héber' : 0,
            'német' : 0,
            'arab' : 0,
            'spanyol' : 0,
            'olasz' : 0,
            'szerb' : 0,
            'jiddis' : 0,
            'portugál' : 0,
            'perzsa' : 0,
            'japán' : 0,
            'Búr' : 0,
            'szláv' : 0,
            'török' : 0,
            'szanszkrit' : 0,
            'indiai' : 0,
            'roma' : 0,
            'orosz' : 0,
            'román' : 0,
            'hindi' : 0,
            'tibeti' : 0,
            'kelta' : 0,
            'szlovák' : 0,
            'lengyel' : 0,
            'tatár' : 0,
            'holland' : 0,
            'arámi' : 0,
            'ukrán' : 0,
            'polinéz' : 0,
            'skót' : 0,
            'cseh' : 0,
            'maláji' : 0,
            'horvát' : 0,
            'indonéz' : 0,
            'kínai' : 0,
            'svéd' : 0,
            'skandináv' : 0,
            'Óskandináv' : 0,
            'egyiptomi' : 0,
            'sémi' : 0
            }
    
    @property
    def Cím(self):
        return self.__Cím
    @Cím.setter
    def Cím(self, cím):
        self.__Cím = cím
        
    @property
    def Szavak_száma(self):
        return self.__Szavak_száma
    @Szavak_száma.setter
    def Szavak_száma(self, szám):
        self.__Szavak_száma = szám
        
    @property
    def Dátum(self):
        return self.__Dátum
    @Dátum.setter
    def Dátum(self, dátum):
        self.__Dátum = dátum
        
    @property
    def Idegen_szavak_száma(self):
        return self.__Idegen_szavak_száma
    @Idegen_szavak_száma.setter
    def Idegen_szavak_száma(self, szama):
        self.__Idegen_szavak_száma+=szama

    @property
    def Idegen_szavak(self):
        return self.__Idegen_szavak
    @Idegen_szavak.setter
    def Idegen_szavak(self, nyelv):
        for i in list(self.__Idegen_szavak.keys()):
            if (i in nyelv.split('-')) or (i in nyelv.split('+')):
                self.__Idegen_szavak[i]+=1
    def Kiír(self):
        ch = ";"
        result = [(self.__Cím +ch+ str(self.__Szavak_száma) +ch+ self.__Dátum +ch+ str(self.__Idegen_szavak_száma))]
        for i in self.__Idegen_szavak.values():
            result.append(ch)
            result.append(str(i))
        return (' '.join(result) + '\n')
            
        

#create a driver
s = Service('C:/Users/benif/Downloads/chromedriver_win32/chromedriver.exe')

#1988-2005
driver = webdriver.Chrome(service=s)
url = 'https://archiv1988-2005.mti.hu/Pages/HirSearch.aspx?Pmd=1'
wait = WebDriverWait(driver, 120)
dátumok = []
for év in range(2022, 1991, -1):
    for hónap in range(12, 0, -1):
        if hónap>9:
            dátumok.append(str(év)+"."+str(hónap)+"."+"20.")
            dátumok.append(str(év)+"."+str(hónap)+"."+"10.")
            dátumok.append(str(év)+"."+str(hónap)+"."+"01.")
        else:
            dátumok.append(str(év)+".0"+str(hónap)+"."+"20.")
            dátumok.append(str(év)+".0"+str(hónap)+"."+"10.")
            dátumok.append(str(év)+".0"+str(hónap)+"."+"01.")
dátumok = dátumok[30:-3]
for i in dátumok:
    print(i)

# igaz = True
címek=[]
driver.get(url)
for n in range(len(dátumok)-1):
    kifile = open('statisztika'+str(n)+'.csv', 'wt', encoding="utf-16")
    wait.until(EC.presence_of_element_located((By.ID, 'ctl00_SearchPlaceHolder_SearchPageControl1_ChkBoxTableControl1_ChkBoxControl_2')))

    #checkboxok
    if n==0:
        driver.find_element(By.ID, "ctl00_SearchPlaceHolder_SearchPageControl1_ChkBoxTableControl1_ChkBoxControl_2").click()
        driver.find_element(By.ID, "ctl00_SearchPlaceHolder_SearchPageControl1_ChkBoxTableControl1_ChkBoxControl_4").click()

    #ide kellen jöjjön a dátumok beírása
    kezd = driver.find_element(By.ID, 'ctl00_SearchPlaceHolder_SearchPageControl1_SearchDateSt')
    kezd.clear()
    kezd.send_keys(dátumok[n+1])
    vege = driver.find_element(By.ID, 'ctl00_SearchPlaceHolder_SearchPageControl1_SearchDateEd')
    vege.clear()
    vege.send_keys(dátumok[n])
    #keresés gomb
    driver.find_element(By.ID,'ctl00_SearchPlaceHolder_SearchPageControl1_Button1').click()
    #tartalom táblázat egy már megnyitott oldalon
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tartalom")))
    ch=";"
    nyelvek = ""
    for i in Item().Idegen_szavak.keys():
        nyelvek += ch + i
    kifile.write(
                "Cím" +ch+
                "Szavak száma" +ch+
                "Dátum" +ch+
                "Idegen szavak száma" +
                nyelvek + '\n'
                 )
    sorszam=7
    driver.find_element(By.ID, 'ctl00_SearchPlaceHolder_PDFsearchList1_lvNewsList_ctrl0_HyperLink1').click()
    open_read_close_articles()
    n+=1
    kifile.close()
    time.sleep(2)
    print("A főprogram while-ja lefutott egyszer")
    
driver.quit()    
