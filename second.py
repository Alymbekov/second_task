import re
pattern = r"\d+"
sentence = "12 ай, 12 жыл 12 үй 12 киши"
sentence = re.findall(pattern,sentence)
sen = str(sentence)
print(sen)