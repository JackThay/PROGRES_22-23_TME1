'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Server side of ex1 from TME1, with a 1-2 chance for the server not to respond
'''
from socket import *
import random

# >>> Code inspired from professor's slides <<<
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",serverPort))

# >> Generating a 1/2 chance for the server to forget answering a ping request
def half_chance():
    list_chance05 = [0, 1]
    chance05 = random.choice(list_chance05)
    return chance05

# >> Launching server <<
print(">>>Server ready, waiting for ping...")
while True:
    ping, clientAddress = serverSocket.recvfrom(2048)
    pong = bytes(1)
    if(half_chance()==1):
        serverSocket.sendto(pong,clientAddress)
        print("I remembered that I have to answer the Ping request")
    else:
        print("I forgot to answer the ping request")

