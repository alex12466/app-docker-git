import re
with open("input.txt" , "r") as file:
	content = file.read()
print(content)

text_fara_spatii = re.sub(r'\s+' , ' ',file)

print("Text dupa eliminare spatii : ", text_fara_spatii)

