
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PAROPEN',
    'PARCLOSE'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PAROPEN = r'\('
t_PARCLOSE = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int (t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()

data = '''
3 + 4 * 10
  + -20 *2
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)