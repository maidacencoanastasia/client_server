import socket

def main():
    host = '127.0.0.1'
    port = 8000
    s = socket.socket.connect(host, port)
    while True:
        data = s.recv(1024)
        if not data:
               break
        print(data.decode('utf-8'))
        if data.endswith(b"(1-9): "):
            player_move = input()
            s.sendall(player_move.encode('utf-8'))
        else:
            data = s.recv(1024)
            print(data.decode('utf-8'))
    print('Connection closed.')

if __name__ == '__main__':
    main()
