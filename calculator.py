def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def get_result(expression):
    if '(' in expression:
        start = 0
        for i in range(len(expression)):
            if expression[i] == '(':
                start = i
        fin = start + expression[start:].index(')')
        temp = expression[start+1:fin]
        result = get_result(temp)
        return get_result(f'{expression[:start]}{result}{expression[fin+1:]}')

    sign = ''
    for s in '+-*/':
        if s in expression:
            sign = s
            break
    if sign == '':
        return int(expression)
    else:
        a, b = expression.split(sign, 1)
        if sign == '*': return mult(get_result(a), get_result(b))
        if sign == '/': return div(get_result(a), get_result(b))
        if sign == '+': return summ(get_result(a), get_result(b))
        if sign == '-': return diff(get_result(a), get_result(b))

ex = input('Введите выражение\n')

print(get_result(ex))
