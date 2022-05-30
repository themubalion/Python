import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
# url = input('Enter the URL')
command = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysocket.send(command)
while True:
    data = mysocket.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysocket.close