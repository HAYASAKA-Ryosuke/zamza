#!coding:utf-8
import ply.yacc as yacc
from lexanalysis import tokens


def p_expression_factor(p):
    '''expression : factor'''
    p[0] = {'type': 'stiring', 'name': p[1]}


def p_expression_wire(p):
    'expression : term WIRE term'
    p[0] = [p[1], p[3]]


def p_term_dot(p):
    '''term : factor DOT factor'''
    p[0] = {'name': p[1], 'pin': p[3]}


def p_term_end(p):
    '''expression : END'''
    p[0] = p[1]


def p_expression_import(p):
    '''expression : IMPORT STRING'''
    p[0] = {'type': 'import', 'name': p[2]}


def p_expression_package(p):
    '''expression : PARTS STRING COLON'''
    p[0] = {'type': 'parts', 'name': p[2]}


def p_factor_string(p):
    '''factor : STRING'''
    p[0] = p[1]
    print(p[0])


def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

if __name__ == '__main__':
    data = '''
    #test
    parts A:
    #    B;C;
    #end
    #A1.B - C1.D
    '''
    data1 = '''
    parts A:
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
    result = parser.parse(data1)
    result = parser.parse(data1)
    if result['type'] == 'parts':
        print(result['name'])
        result = parser.parse(data2)
        print(result)
        result = parser.parse(data3)
        print(result)
        result = parser.parse(data4)
        print(result)
        if result != 'end':
            print('error')
    result = parser.parse(data5)
    print(result)
    #result = parser.parse(data3)
    #print(result)
    #for line in data.split('\n'):
    #    result = parser.parse(line)
    #    print(result)
    #    #if result['type'] == 'parts':
    #    #    print(result['name'])
