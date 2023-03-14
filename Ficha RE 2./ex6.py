import re 

matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

sep1 = r"(?P<sep>[ -])"
sep2 = r"(?P=sep)"
NN = r"[0-9]{2}"
LL = r"[A-Z]{2}"

validas = [
    LL + sep1 + LL + sep2 + NN,
    LL + sep1 + NN + sep2 + LL,
    NN + sep1 + LL + sep2 + LL,
    LL + sep1 + NN + sep2 + NN,
    NN + sep1 + NN + sep2 + LL,
    NN + sep1 + LL + sep2 + NN
    ]

def matricula_valida(matricula):
  return any(re.fullmatch(valida,matricula) for valida in validas)


for matricula in matriculas:
  print (matricula_valida(matricula))