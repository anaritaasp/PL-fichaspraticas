import ply.lex as lex

tokens = (
'PALAVRA',
'VIRGULA',
'PONTOI',
'PONTOE',
'PONTOF',
'RETS'
)

t_PALAVRA = r'[\w\-]+'
t_VIRGULA = r','
t_PONTOI = r'\?'
t_PONTOE = r'\!'
t_PONTOF = r'\.'
t_RETS = r'\.{3,}'

t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("Olá, eu chamo-me Sofia!")

while tok := lexer.token():
    print(tok)
 