import re

def narcissismo(linha):
  str = re.findall(r"([eE][uU])",linha)
  return len(str)

print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))