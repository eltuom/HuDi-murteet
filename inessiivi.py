import sys
import re
from collections import Counter

etsittavat_sanat = ["koulu", "koulus", "koulusa", "paikka", "paikas", "paikasa", "paikaisin", "hukassa", "hukas", "hukasa", "hukka", "töissä", "töis", "töisä",]

yleiskielinen = []
lantinen_kato = []
lantinen_s = []
muu = []   # tänne kerätään muut muodot

laskuri = Counter()

def annojen_erittely(line):
    pattern = r"'.*?'"
    annot = re.findall(pattern, line)
    annot = [i.strip("'") for i in annot]
    return annot

for line in sys.stdin:
    annorivi = annojen_erittely(line)
    if len(annorivi) >= 2:
        etsittava_sana = annorivi[2].lower()
        if etsittava_sana in etsittavat_sanat:
          if "kk" not in annorivi[1]: # tällä varmistetaan inessiivit koska kk:k vaihtelu
              if "ssa" in annorivi[1].lower():
                  yleiskielinen.append(annorivi)
              elif "sa" in (annorivi[1]).lower() and "ss" not in annorivi[1].lower() and "Case=Ine" in annorivi[5]:
                  lantinen_s.append(annorivi)
              elif "s" in (annorivi[1])[-1].lower():
                  lantinen_kato.append(annorivi)
              else:
                  muu.append(annorivi)

# prosentteja varten
total_matches = len(yleiskielinen) + len(lantinen_kato) + len(lantinen_s)

if total_matches > 0:
    percentages = {
        "Yleiskielinen pääte": len(yleiskielinen) / total_matches * 100,
        "Muut läntiset s-päätteet (kato)": len(lantinen_kato) / total_matches * 100,
        "Päätteenä kaksoiskonsonantin supistuminen eli paikasa": len(lantinen_s) / total_matches * 100,
    }

    for key, value in percentages.items():
        print(f"{key} osuus esiintymistä: {value:.2f}%")
    print()

# esiintymät ulos, taman voi poistaa jos tarve vaan frekvensseille
print("Kaikki yleiskieliset esiintymät:", len(yleiskielinen))
print("Ei eritellä yleiskielisiä esiintymiä")
print("Muut läntiset s-päätteet (kato):", len(lantinen_kato))
#for item in lantinen_kato:
#    print(item)
print("Kaikki kaksoiskonsonantin supistumiset eli paikasa:", len(lantinen_s))
for item in lantinen_s:
    print(item)
print("Muut esiintymät:", len(muu))
print("Ei eritellä muita")
