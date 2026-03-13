import re
import json

with open("saarnoja.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"^\s*(\d{1,3})\."

matches = list(re.finditer(pattern, text, re.MULTILINE))

sermons = []
expected = 1

for i, match in enumerate(matches):

    number = int(match.group(1))

    # hyväksy vain oikea seuraava saarna
    if number != expected:
        continue

    start = match.start()

    # etsitään seuraava osuma
    if i < len(matches) - 1:
        end = matches[i + 1].start()
    else:
        end = len(text)

    sermon_text = text[start:end].strip()

    lines = sermon_text.split("\n")

    title = lines[0].strip()
    body = "\n".join(lines[1:]).strip()

    sermons.append({
        "id": number,
        "title": title,
        "text": body
    })

    expected += 1

    if expected > 466:
        break


with open("lll_sermons.json", "w", encoding="utf-8") as f:
    json.dump(sermons, f, ensure_ascii=False, indent=2)


print("Valmis!")
print("Saarnoja löytyi:", len(sermons))
print("Ensimmäinen:", sermons[0]["title"])
print("Viimeinen:", sermons[-1]["title"])