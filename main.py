import re
with open("input.txt" , "r") as file:
	content = file.read()
print(content)

text_fara_spatii = re.sub(r'\s+' , ' ',file)

text_fara_punctuatie = re.sub(r'[^\w\s]', '',text_fara_spatii)
print("Text fara punctuatie : " , text_fara_punctuatie)

