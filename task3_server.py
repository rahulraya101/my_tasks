import socket
import uuid
from _thread import *

ServerSocket8000 = socket.socket()
ServerSocket8001 = socket.socket()

host = '127.0.0.1'
port_8000 = 8000
port_8001 = 8001

uuids = {}

try:
    ServerSocket8000.bind((host, port_8000))
    ServerSocket8001.bind((host, port_8001))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')

ServerSocket8000.listen(5)
ServerSocket8001.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        user_uuid = data.decode('utf-8')
        if not uuids[user_uuid]:
            uuids[user_uuid] = str(uuid.uuid4())
        reply = 'Server uuid: ' + uuids[user_uuid]
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


def threaded_client_8001(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        resp = str(data.decode('utf-8')).split('|')
        if resp[2] == uuids[resp[1]]:
            reply = 'Text message was saved.'
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(str(resp[0]) + '\n')
                f.write('-------------------------------------------------------------------------------------')
                f.write('\n')
            connection.sendall(str.encode(reply))
        else:
            reply = 'Wrong uuid! Please provide the correct one.'
            connection.sendall(str.encode(reply))

        if not data:
            break
    connection.close()


try:
    while True:
        Client_8000, address_8000 = ServerSocket8000.accept()
        Client_8001, address_8001 = ServerSocket8001.accept()
        print('Connected to: ' + address_8000[0] + ':' + str(address_8000[1]))
        print('Connected to: ' + address_8001[0] + ':' + str(address_8001[1]))
        start_new_thread(threaded_client, (Client_8000,))
        start_new_thread(threaded_client_8001, (Client_8001,))
except KeyboardInterrupt:
    print('Interrupted!')
finally:
    ServerSocket8000.close()
    ServerSocket8001.close()