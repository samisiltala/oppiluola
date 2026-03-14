import re, json

verses=[]

book=""
chapter=0

with open("raamattu.txt",encoding="utf8") as f:

    for line in f:

        line=line.strip()

        # kirjan nimi
        if "MOOSEKSEN KIRJA" in line:
            book=line.lower()

        # luku
        m=re.match(r"(\d+)\s+LUKU",line)
        if m:
            chapter=int(m.group(1))

        # jae
        m=re.match(r"(\d+):(\d+)\s+(.*)",line)
        if m:

            verses.append({
                "book":book,
                "chapter":int(m.group(1)),
                "verse":int(m.group(2)),
                "text":m.group(3)
            })

with open("bible.json","w",encoding="utf8") as f:
    json.dump(verses,f,ensure_ascii=False)