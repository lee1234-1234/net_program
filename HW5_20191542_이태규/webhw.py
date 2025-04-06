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

def handle_client(client_socket):
    # 클라이언트로부터 요청 읽기
    request = client_socket.recv(1024).decode()
    if not request:
        client_socket.close()
        return

    print("요청 내용:")
    print(request)
    
    # 요청 라인 파싱 (예: "GET /index.html HTTP/1.1")
    request_line = request.split("\r\n")[0]
    parts = request_line.split()
    if len(parts) < 2:
        client_socket.close()
        return
    
    # 요청한 자원 (파일 이름) 얻기
    path = parts[1]
    filename = path.lstrip('/')
    if filename == "":
        filename = "index.html"  # 기본 파일
    
    try:
        # 파일이 text인지 binary에 따라 읽기 모드 설정
        if filename.endswith(".html"):
            # index.html의 경우 'r' 모드, 필요시 'euc-kr' 인코딩 사용 가능
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            content_bytes = content.encode('utf-8')
        else:
            with open(filename, 'rb') as f:
                content_bytes = f.read()
        
        mime_type = get_mime_type(filename)
        # HTTP 응답 헤더 작성
        response_line = "HTTP/1.1 200 OK\r\n"
        response_headers = f"Content-Type: {mime_type}\r\n\r\n"
        response = response_line + response_headers
        # 헤더와 파일 내용을 전송
        client_socket.send(response.encode() + content_bytes)
    
    except Exception as e:
        print(f"파일 {filename}을(를) 찾을 수 없습니다: {e}")
        # 파일이 없을 경우 404 Not Found 응답
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "\r\n"
        response_body = (
            "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>"
            "<BODY>Not Found</BODY></HTML>"
        )
        response = response_line + response_headers + response_body
        client_socket.send(response.encode())
    
    client_socket.close()

def run_server():
    # 포트 80번 사용 시 관리자 권한 필요
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 80))
    server_socket.listen(10)
    print("웹 서버 시작됨. 클라이언트 연결 대기 중...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print("연결 요청 from", addr)
        handle_client(client_socket)

if __name__ == '__main__':
    run_server()
