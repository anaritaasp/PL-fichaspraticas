import re

lista = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]
listinha=[]
for elem in lista:
  regex=re.split('-(?!-)',elem)
  if len(regex)>1:
    #print(regex[0])
    if re.match("[0-9]{4}$", regex[0]):
      if re.match("[0-9]{3}$", regex[1]):
        tuploo =(regex[0], regex[1])
        listinha.append(tuploo)
print (listinha)
  

