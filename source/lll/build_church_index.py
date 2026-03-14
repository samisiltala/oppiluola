import json
import re

index={}
current=None

with open("saarnoja.txt",encoding="utf8") as f:

    start=False

    for line in f:

        line=line.strip()

        if not line:
            continue

        # aloita vasta Aiheluettelon jälkeen
        if line.startswith("Aiheluettelo"):
            start=True
            continue

        if not start:
            continue

        # kirkkovuoden otsikko (ei ala numerolla)
        if not re.match(r"^\d",line):

            current=line
            index[current]=[]
            continue

        # saarnanumero
        nums=re.findall(r"\d+",line)

        if current:
            index[current].extend([int(n) for n in nums])

# poista tyhjät
index={k:v for k,v in index.items() if v}

with open("church_year.json","w",encoding="utf8") as f:
    json.dump(index,f,ensure_ascii=False,indent=2)

print("valmis:",len(index),"kirkkovuoden kohtaa")