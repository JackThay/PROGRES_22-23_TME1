'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Client side of ex1 from TME1, with a 1-2 chance for the server not to respond
'''
from socket import *
import time


# >>> Code inspired from professor's slides <<<
serverName = "127.0.0.1" #Write down here the destination's IP
serverPort = 1234 #Write down here the destination's port
clientSocket = socket(AF_INET,SOCK_DGRAM)


ping = bytes(1)

# >> Sending Ping <<
#print(">Sending Ping...")
#start_pingtime=time.time()
#clientSocket.sendto(ping,(serverName,serverPort))

# >> Recceiving Pong <<
#pong, serverAddress = clientSocket.recvfrom(2048)
#finish_pingtime=time.time()
#print(">Pong received!")

# >> Displaying received message <<
#pingtime=finish_pingtime-start_pingtime
#print("== Received modified message :" + str(pong.decode("utf-8")) + " ==")
#print("== Ping time was :" + str(pingtime) +" ==")
#clientSocket.close()

# >> Error Message << 
try:
    print(">Sending Ping...")
    start_pingtime=time.time()
    clientSocket.sendto(ping,(serverName,serverPort))
    clientSocket.settimeout(1.0)
    pong, serverAddress = clientSocket.recvfrom(2048)
    finish_pingtime=time.time()
    print(">Pong received!")
    pingtime=finish_pingtime-start_pingtime
    print("== Received modified message :" + str(pong.decode("utf-8")) + " ==")
    print("== Ping time was :" + str(pingtime) +" ==")
    clientSocket.close()
except timeout:
    print("The server didn't answer back")