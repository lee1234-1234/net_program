from socket import *

def get_mime_type(filename):
    if filename.endswith(".html"):
        return "text/html; charset=utf-8"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".ico"):
        return "image/x-icon"
    else:
        return "application/octet-stream"

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    if len(req) > 0:
        request_line = req[0]
        tokens = request_line.split()
        if len(tokens) >= 2:
            path = tokens[1]
            filename = path.lstrip('/')
            if filename == "":
                filename = "index.html"
            
            try:
                mime = get_mime_type(filename)
                if filename.endswith(".html"):
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    body = content.encode('utf-8')
                else:
                    with open(filename, 'rb') as f:
                        body = f.read()
                
                resp_line = "HTTP/1.1 200 OK\r\n"
                resp_headers = "Content-Type: " + mime + "\r\n\r\n"
                resp = resp_line + resp_headers
                c.send(resp.encode() + body)
            except Exception as e:
                print("파일을 찾을 수 없음:", filename, e)
                resp_line = "HTTP/1.1 404 Not Found\r\n"
                resp_headers = "\r\n"
                resp_body = "<html><head><title>Not Found</title></head><body>Not Found</body></html>"
                resp = resp_line + resp_headers + resp_body
                c.send(resp.encode())
    c.close()
