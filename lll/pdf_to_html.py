import fitz

pdf = fitz.open("post_fix.pdf")

html = ""

for page in pdf:
    html += page.get_text("html")

with open("saarnat.html", "w", encoding="utf8") as f:
    f.write(html)

print("Valmis!")