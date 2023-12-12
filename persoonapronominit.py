import sys
import re
from collections import Counter

etsittavat_sanat = ["mä", "mää", "sä", "sää", "mie", "miä", "sie", "siä", "minä", "sinä"]

mä_sä = []
mie_sie = []
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
        if (etsittava_sana in etsittavat_sanat and 
            "PRON" in annorivi[3] and 
            "l" not in annorivi[1] and 
            len(annorivi[1]) > 1 and 
            any(word in annorivi[1] for word in ["mä", "sä", "mie", "sie"])
           ):
            if "mä" in etsittava_sana or "sä" in etsittava_sana:
                mä_sä.append(annorivi)
            elif "mie" in etsittava_sana or "sie" in etsittava_sana:
                mie_sie.append(annorivi)

# lasketaan kaikki esiintymät ja osuudet
total_matches = len(mä_sä) + len(mie_sie) + len(muu)

if total_matches > 0:
    percentages = {
        "Läntinen mä tai sä": len(mä_sä) / total_matches * 100,
        "Itäinen mie tai sie": len(mie_sie) / total_matches * 100,
        "Muut esiintymät": len(muu) / total_matches * 100,
    }

    for key, value in percentages.items():
        print(f"{key} osuus esiintymistä: {value:.2f}%")
    print()

# esiintymät ulos
print("Kaikki läntiset:", len(mä_sä))
for item in mä_sä:
    print(item)
print("Kaikki itäiset:", len(mie_sie))
for item in mie_sie:
    print(item)
print("Kaikki muut esiintymät:", len(muu))
for item in muu:
    print(item)
