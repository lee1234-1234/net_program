import socket
import time

def request_device(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    s.send("Request".encode())
    data = s.recv(1024).decode()
    s.close()
    return data

def send_quit(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    s.send("quit".encode())
    data = s.recv(1024).decode()
    s.close()
    print(f"Device (port {port}) 응답: {data}")

def main():
    device1_port = 1001
    device2_port = 1002
    data_file = "data.txt"
    
    while True:
        cmd = input("Enter 1 (Device1), 2 (Device2), or quit: ").strip()
        if cmd == "1":
            result = request_device(device1_port)
            timestamp = time.ctime()
            log_line = f"{timestamp}: Device1: {result}\n"
            with open(data_file, "a", encoding="utf-8") as f:
                f.write(log_line)
            print("수집된 데이터:", log_line)
        elif cmd == "2":
            result = request_device(device2_port)
            timestamp = time.ctime()
            log_line = f"{timestamp}: Device2: {result}\n"
            with open(data_file, "a", encoding="utf-8") as f:
                f.write(log_line)
            print("수집된 데이터:", log_line)
        elif cmd.lower() == "quit":
            send_quit(device1_port)
            send_quit(device2_port)
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 1, 2, quit 중 하나를 입력하세요.")

if __name__ == '__main__':
    main()
