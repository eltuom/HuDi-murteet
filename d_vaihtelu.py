import sys
import re
from collections import Counter

etsittavat_sanat = ["syödä", "syydä", "syörä", "syyvä", "syvvä", "kären", "käsi", "käjen", "rauva", "rauta", "raura", "tehrä", "tehä",]

yleiskielinen = []
lantinen_r = []
itainen_v = []
muu = []

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
            if "d" in annorivi[1].lower():          # yleiskielinen d
                yleiskielinen.append(annorivi)
            elif len(etsittava_sana) >= 4 and "r" in etsittava_sana[2].lower() or "r" in etsittava_sana[3].lower() : # läntinen r
                lantinen_r.append(annorivi)
            elif "v" in annorivi[1].lower() and "yö" not in etsittava_sana:   # itäinen v
                itainen_v.append(annorivi)
            else:
                muu.append(annorivi)

# lasketaan kaikki esiintymät ja osuudet
total_matches = len(lantinen_r) + len(yleiskielinen) + len(itainen_v) + len(muu)

if total_matches > 0:
    percentages = {
    "Läntinen r vaihtelu": len(lantinen_r) / total_matches * 100,
    "Yleiskielinen d": len(yleiskielinen) / total_matches * 100,
    "Itäinen v vaihtelu": len(itainen_v) / total_matches * 100,
    "Muut esiintymät": len(muu) / total_matches * 100,
}

    for key, value in percentages.items():
        print(f"{key} osuus esiintymistä: {value:.2f}%")
    print()

# esiintymät näkyviin, poista # tarvittaessa
#print("Kaikki r vaihtelut:", len(lantinen_r))
#for item in lantinen_r:
#    print(item)
# print("Kaikki yleiskieliset variantit:", len(yleiskielinen))
# for item in yleiskielinen:
#    print(item)
#print("Kaikki itäiset v:"), len(itainen_v)
#for item in itainen_v:
#    print(item)
#print("Kaikki muut esiintymät:", len(muu))
#for item in muu:   
#   print(item)
