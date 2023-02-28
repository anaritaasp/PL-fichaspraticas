import re
def troca_de_curso(linha, novo_curso):
  print(re.sub(r"(i?LEI)", novo_curso,linha))

print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.","MIEI"))