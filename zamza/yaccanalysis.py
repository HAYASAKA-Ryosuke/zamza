#!coding:utf-8
import ply.yacc as yacc
from lexanalysis import tokens


def p_term_comma(p):
    pass
#    'term : term COMMA term'
#    p[0] = [p[1], p[3]]
#    print('term_comma')
#    print(p[0])
#
#
def p_term_parts(p):
    'term : PARTS STRING COLON'
    p[0] = p[2]
    print('term_parts')
    print(p[0])


def p_term_dot(p):
    'factor : STRING DOT STRING'
    p[0] = {'name': p[1], 'pin': p[3]}
    print('term_dot')
    print(p[0])


def p_term_wire(p):
    'term : factor WIRE factor'
    p[0] = [p[1], p[3]]
    print('expression_wire')
    print(p[0])


def p_term_paren(p):
    'factor : LEFTPAREN STRING RIGHTPAREN'
    p[0] = p[2]
    print('paren')
    print(p[0])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

if __name__ == '__main__':
    data = '''
    #test
    parts A:
        B, C
    end
    A.B - C.D
    '''
    result = parser.parse(data)
    print(result)
