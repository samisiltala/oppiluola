import fitz

pdf = fitz.open("post_fix.pdf")

text = ""

for page in pdf:
    text += page.get_text()

with open("saarnat.txt", "w", encoding="utf8") as f:
    f.write(text)

print("Valmis!")