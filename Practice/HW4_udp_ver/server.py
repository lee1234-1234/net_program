from socket import *

def calculate(expr):
    try:
        expr = expr.replace(' ', '')
        if '+' in expr:
            a, b = expr.split('+')
            return str(int(a) + int(b))
        elif '-' in expr:
            a, b = expr.split('-')
            return str(int(a) - int(b))
        elif '*' in expr:
            a, b = expr.split('*')
            return str(int(a) * int(b))
        elif '/' in expr:
            a, b = expr.split('/')
            return format(int(a) / int(b), '.1f')
        else:
            return '지원하지 않는 연산'
    except:
        return '잘못된 수식'

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 3333))
print('UDP server is running...')

while True:
    data, addr = s.recvfrom(1024)
    expression = data.decode().strip()
    if expression.lower() == 'q':
        print('Connection closed by', addr)
        continue
    
    result = calculate(expression)
    s.sendto(result.encode(), addr)