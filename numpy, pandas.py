import numpy as np
import pandas as pd
from numpy import genfromtxt

df = pd.read_csv("idegen szavak.csv", delimiter="|", header=0, encoding="utf-16")

eredetek = df["Eredete"].unique()

#a unique value-k alapján az adattisztítás megtervezése

egyedi = [ 'latin', 'görög', 'angol', 'francia', 'héber',
        'német', 'arab',  'spanyol', 'olasz', 'szerb', 'jiddis',
        'portugál', 'perzsa', 'japán', 'Búr', 'szláv', 'török','szanszkrit',
        'indiai',  'roma', 'orosz', 'román', 'hindi',
        'tibeti',  'kelta', 'szlovák', 'lengyel', 'tatár',
        'holland', 'arámi', 'ukrán', 'polinéz', 'skót', 'cseh',
        'maláji','horvát', 'indonéz', 'kínai', 'svéd', 'skandináv',
        'Óskandináv','egyiptomi', 'sémi']


hibás = [ 'farncia','római',  'bajor-osztrák',
         'sváb', 'osztrák', 'viking', 'angolszász', 'lovári',
          'cigány']

felesleges = ['székely', 'nyírség', 'népi', 'nincs adat',
              'ismeretlen', 'magyar','-',
              'Feltehetőleg a jiddis tréfli szóból ered.',
              'Idegen Szavak és Kifejezések Szótára',
              'agrároldal.hu', 'Kvízpart']


#segítség az listak keszitesehez
szavak=""
for i in egyedi:
  szavak+= i + " = 0\n"
print(szavak)

#segítség az osztály létrehozásához
szavak=""
for i in egyedi:
  szavak+="_" + i + " = 0\n"
print(szavak)