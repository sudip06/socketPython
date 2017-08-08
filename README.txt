## Socket program example in python ##

This is a simple implementation of socket program using python.

The server runs on port 9999 and accepts maximum of 5 connections. 
The client sends the timstamp and the server responds back the data
received.

#### Testing ####
Server Side
===========
socket$ 
socket$ python ./server.py 
Listening on 127.0.0.1:9999
Accepted connection from 127.0.0.1:59958
Received 2017-08-08 22:32:02
Accepted connection from 127.0.0.1:59960
Received 2017-08-08 22:32:07
Accepted connection from 127.0.0.1:59962
Received 2017-08-08 22:32:09
Accepted connection from 127.0.0.1:59964
Received 2017-08-08 22:32:11
Accepted connection from 127.0.0.1:59966
Received 2017-08-08 22:32:13


Client Side
===========
socket$ python ./client.py 
Received:ACK! 2017-08-08 22:32:09
socket$ 
socket$ python ./client.py 
Received:ACK! 2017-08-08 22:32:11
socket$ 
socket$ python ./client.py 
Received:ACK! 2017-08-08 22:32:13
socket$ 



#### Authors #####

    Sudip Midya - Initial Work


