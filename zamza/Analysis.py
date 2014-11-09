#!coding:utf-8
import ply.yacc as yacc
import ply.lex as lex


class Parser:
    def __init__(self):
        yacc.yacc(module=self)
        lex.lex(module=self)

    def run(self, val):
        for i in range(len(val.split('\n'))):
            res = self.text(val.split('\n')[i])
            if res is not None:
                if res['type'] == 'ic':
                    self.fic(val.split('\n')[i:])
                if res['type'] == 'import':
                    self.fimport(val.split('\n')[i:])
                if res['type'] == 'main':
                    self.fmain(val.split('\n')[i:])

    def text(self, val):
        return yacc.parse(val)

    def connmas(self, val):
        def _reader():
            yield val.split(",")
        return [i for i in _reader()]

    def fmain(self, val):
        print()
        pass

    def fimport(self, val):
        pass

    def fic(self, val):
        def _direction(i, val):
            reslist = []
            j = i+1
            while True:
                res = self.text(val[j])
                if res is not None:
                    if res['type'] == 'END':
                        return reslist
                    else:
                        reslist.append(res)
                        j += 1
        left = None
        right = None
        bottom = None
        top = None

        for i in range(1, len(val)):
            res = self.text(val[i])
            if res is not None:
                if res['type'] == 'icleft':
                    left = _direction(i, val)
                    print('left')
                    print(left)
                elif res['type'] == 'icright':
                    right = _direction(i, val)
                    print('right')
                    print(right)
                elif res['type'] == 'icbottom':
                    bottom = _direction(i, val)
                    print('bottom')
                    print(bottom)
                elif res['type'] == 'ictop':
                    top = _direction(i, val)
                    print('top')
                    print(top)
            else:
                print("e:"+val[i]+":e")


class Analysis(Parser):

    reserved = {
        'import': 'IMPORT',
        'main': 'MAIN',
        'left': 'LEFT',
        'right': 'RIGHT',
        'bottom': 'BOTTOM',
        'top': 'TOP',
        'ic': 'IC',
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
    t_ENDCODE = r'\;'
    t_WIRE = r'-'
    t_DOT = r'\.'
    t_COLON = r'\:'
    t_COMMA = r','
    t_LEFTPAREN = r'\('
    t_RIGHTPAREN = r'\)'
    t_ignore = r' \n    '

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        foo = self.reserved.get(t.value, 'ID')
        if foo != 'ID':
            t.type = foo
            return t
        else:
            t.type = 'STRING'
            return t

    def t_STRING(self, t):
        r'\w+'
        t.value = str(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("error '%s'" % t.value[0])

    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def p_expression_factor(self, p):
        '''expression : factor'''
        p[0] = {'type': 'string', 'name': p[1]}

    def p_expression_wire(self, p):
        'expression : term WIRE term'
        p[0] = {'type': 'wire', 'list': [p[1], p[3]]}

    def p_term_dot(self, p):
        '''term : factor DOT factor'''
        p[0] = {'name': p[1], 'pin': p[3]}

    def p_term_end(self, p):
        '''expression : END'''
        p[0] = {'type': 'END', 'name': p[1]}

    def p_expression_import(self, p):
        '''expression : IMPORT STRING'''
        p[0] = {'type': 'import', 'name': p[2]}

    def p_expression_main(self, p):
        '''expression : MAIN COLON'''
        p[0] = {'type': 'main', 'name': p[1]}

    def p_expression_package(self, p):
        '''expression : IC STRING COLON'''
        p[0] = {'type': 'ic', 'name': p[2]}

    def p_expression_left(self, p):
        '''expression : LEFT COLON'''
        p[0] = {'type': 'icleft', 'name': p[2]}

    def p_expression_right(self, p):
        '''expression : RIGHT COLON'''
        p[0] = {'type': 'icright', 'name': p[2]}

    def p_expression_bottom(self, p):
        '''expression : BOTTOM COLON'''
        p[0] = {'type': 'icbottom', 'name': p[2]}

    def p_expression_top(self, p):
        '''expression : TOP COLON'''
        p[0] = {'type': 'ictop', 'name': p[2]}

    def p_factor_string(self, p):
        '''factor : STRING'''
        p[0] = p[1]

    def p_error(self, p):
        print("Syntax error")

if __name__ == '__main__':
    data = '''
    #test
    ic A:
        left:
            p1;p2;
        right:
            p3;p4;
    #end
    #A1.B - C1.D
    '''
    data1 = '''
    ic A:
    '''
    data2 = '''
    B
    '''
    data3 = '''
    C
    '''
    data4 = '''
    end
    '''
    data5 = '''
    A2.B - C2.D'''
    parser = Analysis()
    result = parser.text(data1)
    result = parser.text(data1)
    if result['type'] == 'ic':
        print(result['name'])
        result = parser.text(data2)
        print(result)
        result = parser.text(data3)
        print(result)
        result = parser.text(data4)
        print(result)
        if result != 'end':
            print('error')
    result = parser.text(data5)
    print(result)
    #result = parser.parse(data3)
    #print(result)
    #for line in data.split('\n'):
    #    result = parser.parse(line)
    #    print(result)
    #    #if result['type'] == 'parts':
    #    #    print(result['name'])
