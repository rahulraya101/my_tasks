import socket


ClientSocket8000 = socket.socket()
ClientSocket8001 = socket.socket()

host = '127.0.0.1'
port_8000 = 8000
port_8001 = 8001

print('Waiting for connection')

try:
    ClientSocket8000.connect((host, port_8000))
    ClientSocket8001.connect((host, port_8001))
except socket.error as e:
    print(str(e))

Response_8000 = ClientSocket8000.recv(1024)
Response_8001 = ClientSocket8001.recv(1024)

try:
    Input = input('Provide uuid: ')
    ClientSocket8000.send(str.encode(Input))
    Response_8000 = ClientSocket8000.recv(1024)
    print(Response_8000.decode('utf-8'))
    while True:
        Input = input('Provide text message: ') + '|' + input('Provide your uuid: ') + '|' + \
                input('Provide server uuid: ')
        ClientSocket8001.send(str.encode(Input))
        Response_8001 = ClientSocket8001.recv(1024)
        print(Response_8001.decode('utf-8'))
except KeyboardInterrupt:
    print('Interrupted!')
finally:
    ClientSocket8000.close()
    ClientSocket8001.close()