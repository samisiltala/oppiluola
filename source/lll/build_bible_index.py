import re
import json

index={}
current=None

with open("saarnoja.txt",encoding="utf8") as f:
    for line in f:

        line=line.strip()

        if not line:
            continue

        # tunnista raamatunpaikka
        if re.match(r"[A-Za-zÅÄÖåäö]+\.\s*\d+",line):

            ref=line.lower()

            ref=ref.replace(".","")

            # ota kirja + luku
            m=re.match(r"([a-zåäö]+)\s*(\d+)",ref)

            if m:
                key=m.group(1)+" "+m.group(2)
                current=key
                index.setdefault(key,[])

        # tunnista saarnanumero
        elif line.isdigit() and current:

            index[current].append(int(line))

# poista duplikaatit
for k in index:
    index[k]=sorted(list(set(index[k])))

with open("bible_index.json","w",encoding="utf8") as f:
    json.dump(index,f,ensure_ascii=False,indent=2)

print("valmis:",len(index),"raamatunpaikkaa")