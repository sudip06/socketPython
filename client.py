import socket
import datetime

# ipv4 socket created for tcp protocol(SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9999))
timeNow='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

#sending current date and time
client.send(timeNow)

response = client.recv(4096)

print "Received:%s" %response
