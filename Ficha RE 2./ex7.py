import re 

texto = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA]. 
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo. 
Talvez os [GRUPO DE PESSOAS MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""
def preenche(m):
  i = input(f"Introduz um(a) {m.group(1)}: ") 
  return i

re.sub(r"\[([^\]]+)\]",preenche, texto)