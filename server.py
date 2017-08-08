import socket
import threading

bindIp = '127.0.0.1'
bindPort = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIp, bindPort))
#max number of simultaneous conections
server.listen(5) 

print 'Listening on {}:{}'.format(bindIp, bindPort)


def handleClientConnection(clientSocket):
    request = clientSocket.recv(4096)
    print 'Received:{}'.format(request)
    clientSocket.send('ACK!%s' %request)
    clientSocket.close()

while True:
    clientSock, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    clientHandler = threading.Thread(
        target=handleClientConnection,
        args=(clientSock,)
    )
    clientHandler.start()
