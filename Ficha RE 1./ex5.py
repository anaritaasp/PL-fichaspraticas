import re

def soma_string(linha):
  newList = re.split(r",",linha)
  soma = 0
  for i in newList :
    soma += int(i)
  return soma


print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))