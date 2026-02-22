import re
with open("input.txt" , "r") as file:
	content = file.read()
print(content)

text_fara_spatii = re.sub(r'\s+' , ' ',file)

text_fara_punctuatie = re.sub(r'[^\w\s]', '',text_fara_spatii)
text_lower = text_fara_punctuatie.lower()
cuvinte_filtrate = " ".join([w for w in text_lower.split() if len(w) > 3])
print("Rezultat final : " , cuvinte_filtrate)

