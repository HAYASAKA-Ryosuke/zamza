#!coding:utf-8
import ply.lex as lex

tokens = (
        'STRING',
        'WIRE',
        'DOT',
        'NUMBER',
        'LEFTPAREN',
        'RIGHTPAREN',
        )

t_WIRE = r'-'
t_DOT = r'\.'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'


def t_STRING(t):
    r'\w+'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    print("error '%s'" % t.value[0])


def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    #test
    A.B-C.D(10)
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
