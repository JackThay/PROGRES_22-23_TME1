'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Server side of ex1 from TME1
'''
from socket import *
import random

# >>> Code inspired from professor's slides <<<
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",serverPort))

# >> Launching server <<
print(">>>Server ready, waiting for ping...")
while True:
    ping, clientAddress = serverSocket.recvfrom(2048)
    pong = bytes(1)
    serverSocket.sendto(pong,clientAddress)