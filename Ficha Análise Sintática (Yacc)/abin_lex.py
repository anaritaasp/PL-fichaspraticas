import ply.lex as lex

tokens = (
    'AP',
    'FP',
    'VAL'
)

t_AP = r'\('
t_FP = r'\)'
t_VAL = r'\d+'

t_ignore = " \t\n" 

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    lexer.input("( 5 (3 (1 () ()) ()) (8 () (10 () ())))")
    for tok in lexer:
        print(tok)