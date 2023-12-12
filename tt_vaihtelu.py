import sys
import re
from collections import Counter

etsittavat_sanat = ["metsä", "mettä", "mehtä", "mehttä", "messä", "kahtoa", "katsoa", "kattoa", "itte", "itse", "ihte", "ruotti", "ruotsi", "ruohti", ]

tt_vaihtelu = []
ts_vaihtelu = []
t_vaihtelu = []
ht_vaihtelu = []
ss_vaihtelu = []
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
            if "ts" in annorivi[1].lower():
                ts_vaihtelu.append(annorivi)
            elif "tt" in annorivi[1].lower():
                tt_vaihtelu.append(annorivi)
            elif "ht" in annorivi[1].lower():
                ht_vaihtelu.append(annorivi)
            elif "ss" in annorivi[1].lower() and "ts" not in annorivi[1].lower():
                ss_vaihtelu.append(annorivi)
            elif "t" in annorivi[1].lower() and "h" not in annorivi[1].lower() and "ts" not in annorivi[1].lower() and "tt" not in annorivi[1].lower():
                t_vaihtelu.append(annorivi)
            else:
                muu.append(annorivi)

# lasketaan kaikki esiintymät ja osuudet
total_matches = len(tt_vaihtelu) + len(ts_vaihtelu) + len(t_vaihtelu) + len(ht_vaihtelu) + len(muu)

if total_matches > 0:
    percentages = {
        "tt_vaihtelu": len(tt_vaihtelu) / total_matches * 100,
        "ts_vaihtelu": len(ts_vaihtelu) / total_matches * 100,
        "ss_vaihtelu": len(ss_vaihtelu) / total_matches * 100,
        "t_vaihtelu": len(t_vaihtelu) / total_matches * 100,
        "ht_vaihtelu": len(ht_vaihtelu) / total_matches * 100,
        "muu": len(muu) / total_matches * 100,
    }

    for key, value in percentages.items():
        print(f"{key} osuus esiintymistä: {value:.2f}%")
    print()

# Print the occurrences
print("Kaikki tt esiintymät:", len(tt_vaihtelu))
print("Kaikki ts esiintymät:", len(ts_vaihtelu))
print("Kaikki ss esiintymät:", len(ss_vaihtelu))
for item in ss_vaihtelu:
    print(item)
print("Kaikki t+kato esiintymät:", len(t_vaihtelu))
print("Kaikki ht esiintymät:", len(ht_vaihtelu))
print("Muut esiintymät:", len(muu))
for item in muu:
    print(item)
