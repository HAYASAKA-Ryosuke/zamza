#!coding:utf-8
import ply.yacc as yacc
import ply.lex as lex


class Parser:
    def __init__(self):
        yacc.yacc(module=self)
        lex.lex(module=self)
        self.ic_info = []
        self.main_info = []

    def _main_separate(self, code):
        text = ""
        main_line = False
        for code_line in code.split('\n'):
            if "end" in code_line and main_line:
                text += code_line + '\n'
                return text
            elif "main:" in code_line:
                main_line = True
                text += code_line + '\n'
            elif main_line:
                text += code_line + '\n'

    def _ic_separate(self, code):
        text = ""
        res = []
        end_line = False
        for code_line in code.split('\n'):
            if "end" in code_line:
                end_line = True
            if "ic" in code_line and ":" in code_line and end_line:
                res.append(text)
                text = code_line + '\n'
                end_line = False
            elif "main:" in code_line:
                res.append(text)
            else:
                text += code_line + '\n'
        return res

    def run(self, val):
        val = val.strip()
        shapeval = "".join(map(str, [x.replace(',', '\n') for x in val]))
        source_code = self._ic_separate(shapeval)
        source_code.extend([self._main_separate(shapeval)])
        print(source_code)
        for code in source_code:
            for i in range(len(code.split('\n'))):
                res = self.text(code.split('\n')[i])
                if res is not None:
                    if res['type'] == 'ic':
                        self.ic_info.append(self.fic(code.split('\n')[i:]))
                    if res['type'] == 'import':
                        self.fimport(code.split('\n')[i:])
                    if res['type'] == 'main':
                        self.main_info.extend(self.fmain(code.split('\n')[i:]))
        #for code in self._main_separate(shapeval):
        #    for i in range(len(code.split('\n'))):
        #        res = self.text(code.split('\n')[i])
        #        if res is not None:

    def text(self, val):
        return yacc.parse(val)

    def fmain(self, val):
        return self._direction(0, val)

    def fimport(self, val):
        pass

    def _direction(self, i, val):
        reslist = []
        j = i + 1
        while True:
            res = self.text(val[j])
            if res is not None:
                if res['type'] == 'END':
                    return reslist
                else:
                    reslist.append(res)
                    j += 1

    def fic(self, val):
        left = None
        right = None
        bottom = None
        top = None
        name = self.text(val[0])['name']

        for i in range(1, len(val)):
            if val[i] != '':
                res = self.text(val[i])
                if res is not None:
                    if res['type'] == 'ic_left':
                        left = self._direction(i, val)
                    elif res['type'] == 'ic_right':
                        right = self._direction(i, val)
                    elif res['type'] == 'ic_bottom':
                        bottom = self._direction(i, val)
                    elif res['type'] == 'ic_top':
                        top = self._direction(i, val)
        return {'ic_name': name, 'top': top, 'top_len': len(top), 'right': right, 'right_len': len(right), 'left': left, 'left_len': len(left), 'bottom': bottom, 'bottom_len': len(bottom)}


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
    ] + list(reserved.values())
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
        p[0] = {'type': 'ic_left', 'name': p[2]}

    def p_expression_right(self, p):
        '''expression : RIGHT COLON'''
        p[0] = {'type': 'ic_right', 'name': p[2]}

    def p_expression_bottom(self, p):
        '''expression : BOTTOM COLON'''
        p[0] = {'type': 'ic_bottom', 'name': p[2]}

    def p_expression_top(self, p):
        '''expression : TOP COLON'''
        p[0] = {'type': 'ic_top', 'name': p[2]}

    def p_factor_string(self, p):
        '''factor : STRING'''
        p[0] = p[1]

    def p_error(self, p):
        print(p)
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
