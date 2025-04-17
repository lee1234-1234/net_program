from socket import *
import re

def calculate_expression(expression):
    try:
        return round(eval(expression), 1)
    except Exception as e:
        return str(e)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        expression = data.decode().strip()
        if expression.lower() == 'q':
            break
        
        result = calculate_expression(expression)
        client.send(str(result).encode())
    
    client.close()
