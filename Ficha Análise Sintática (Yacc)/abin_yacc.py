import ply.yacc as yacc

from abin import ABin
from abin_lex import tokens

def p_abin_vazia(p):
    'abin : AP FP'
    p[0] = None

def p_abin_cheia(p):
    'abin : AP VAL abin abin FP'
    p[0] = ABin(p[2], p[3], p[4])

parser = yacc.yacc()

print(parser.parse("( 5 (3 (1 () ()) ()) (8 () (10 () ())))"))