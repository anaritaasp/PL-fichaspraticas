import ply.lex as lex

states = (
    ('multine', 'exclusive'), #temos que por a virgula para o transformar num tuplo
)

tokens = (
    'TEXTO',
    'COMENTARIOI',
    'COMENTARIOM'
)

def t_COMENTARIOI (t):
    r'//.*'
    pass

def t_TEXTO(t):
    r'(.|\n)+?'
    return t

def t_ANY_enter_multiline (t):
    r'/\*'
    t.lexer.comment_level +=1
    t.lexer.begin('multine')

def t_multiline_exit(t):
    r'\*/'
    t.lexer.comment_level -=1
    if t.lexer.comment.level == 0:
        t.lexer.begin('INITIAL')  
     
def t_multiline_TEXTO(t):
    r'(.|\n)'
    pass

lexer = lex.lex()

dados = """ 
/* comment */ ola1

/* comment****comment */ ola2 /*
comment
/* comentário dentro de comentário */
****/ ola3

/*********/

ola4
 mais um pouco // remover comentário inline
FIM
"""

lexer.input(dados)

while tok := lexer.token():
    print(tok)