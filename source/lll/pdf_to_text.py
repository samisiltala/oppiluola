from pdfminer.high_level import extract_text

text = extract_text("Raamattu.pdf")

with open("raamattu.txt","w",encoding="utf8") as f:
    f.write(text)