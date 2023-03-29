import ply.lex as lex

tokens = (
'APR',
'FPR',
'VIRGULA',
'REAL',
'INT',
'PALAVRA',
'BOOL',

)

t_APR = r'\['
t_FPR = r'\]'
t_VIRGULA = r','


def t_REAL(t):
    r'-?\d+\.\d+'
    t.value= float (t.value)
    return t

def t_INT(t):
    r'-?\d+'
    t.value=int (t.value)
    return t

def t_PALAVRA(t):
       r'\w+'
       return t

def t_BOOL(t):
       r'True|False'
       return t

t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("[ 1,5, palavra, False ,3.14, 0, fim]")

while tok := lexer.token():
    print(tok)
 