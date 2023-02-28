import re

#Define a função palavra_magica que recebe uma frase e determina se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.

def palavra_magica(frase):
  return re.search(r"por favor[.!?]+$", frase)!= None

print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))