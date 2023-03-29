import ply.lex as lex

states = (
    ('place', 'inclusive'),
    ('opening', 'inclusive'),
    ('decoration', 'inclusive')
)

tokens = (
    'PLACE_NAME',
    'OPEN',
    'CLOSED',
    'DECORATION_NAME'
)

def t_next_entry(t):
    r'",'
    pass

def t_begin_place(t):
    r'"'
    t.lexer.begin('place')

def t_place_exit(t):
    r'\('
    t.lexer.begin('opening')

def t_place_PLACE_NAME(t):
    r'[^(]+'
    t.lexer.last_place = t.value.strip()

def t_opening_OPEN(t):
    r'open'
    if t.lexer.last_place not in t.lexer.opened_places:
        t.lexer.opened_places[t.lexer.last_place] = []

def t_opening_CLOSED(t):
    r'closed'

def t_opening_end(t):
    r'\)'
    t.lexer.begin('INITIAL')

def t_start_decoration(t):
    r'\['
    t.lexer.begin('decoration')

def t_decoration_DECORATION_NAME(t):
    r'[^\]]+'
    if t.lexer.last_place in t.lexer.opened_places:
        t.lexer.opened_places[t.lexer.last_place].append(t.value)

def t_decoration_exit(t):
    r'\]'
    t.lexer.begin('INITIAL')

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.last_place = None
lexer.opened_places = dict()


data = """
"Springfield (open) [bunny statue]",
"Happyville (closed)", 
"Chocolate Land (open) [Easter eggs]",
"Rabbit Hill
(closed) [chocolate bunnies]",
"Cadbury Castle (open)",
"Peeps Park (closed)",
"Lily Gardens
(open) [butterfly garden]",
"Cocoa Town (open) [chocolate river]",
"Carrot
Cove (closed)",
"Hoppington (open) [bunny hop]",
"Jellybean Junction (closed)",
"Bon Bon Bay (open) [marshmallow chickens]",
"Marshmallow 
Marsh (closed)",
"Candy Cane Canyon (open)",
"Cotton Candy Corner 
(closed)",
"Sugarplum Square (open) [sugarplum fairies]",
"Pudding Plains (closed)
[pudding cups]",
"Gingerbread Village (open)",
"Caramel Castle (closed)
[caramel apples]",
"Lollipop Lane (open)"
"Chirping Forest (open)",
"Carrot Farm (closed)",
"Jellybean Junction 
(open) [jellybean trail]",
"Springfield (closed)",
"Chocolate Land 
(closed)",
"Lily Gardens (closed)"
"""


lexer.input(data)

while tok := lexer.token():
    pass

print(lexer.opened_places)