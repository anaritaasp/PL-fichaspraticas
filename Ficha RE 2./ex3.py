#Escreve um filtro de texto que converte cada nome completo de uma pessoa encontrada num texto fonte, no formato PrimeiroNome SegundoNome [...] UltimoNome para o formato UltimoNome, PrimeiroNome. Por exemplo, "Rui Vieira de Castro" passa a "Castro, Rui". Atenção aos conectores "de", "dos", etc.

import re
texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""

print (re.sub(r"([A-Z]\w+)(\s+([A-Z]\w+|d[oa]s?|de))*\s+([A-Z]\w+)+", r"\1 \4", texto))
