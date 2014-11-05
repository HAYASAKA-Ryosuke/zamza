#!coding:utf-8
import ply.lex as lex

reserved = {
    'import': 'IMPORT',
    'parts': 'PARTS',
    'end': 'END',
}

tokens = [
    'STRING',
    'COLON',
    'WIRE',
    'COMMA',
    'DOT',
    'LEFTPAREN',
    'RIGHTPAREN',
    'ENDCODE',
    'ID',
]+list(reserved.values())

#t_IMPORT = r'import'
#t_END = r'end'
#t_PARTS = r'parts'
t_ENDCODE = r'\;'
t_WIRE = r'-'
t_DOT = r'\.'
t_COLON = r'\:'
t_COMMA = r','
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    foo = reserved.get(t.value, 'ID')
    if foo != 'ID':
        t.type = foo
        return t
    else:
        t.type = 'STRING'
        return t


def t_STRING(t):
    r'\w+'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t\n'


def t_error(t):
    print("error '%s'" % t.value[0])


def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    #test
    import C
    parts A:
        B,C
    end
    A.B-C.D(10)
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
