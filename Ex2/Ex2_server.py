'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Server side of ex2 from TME1
'''
from socket import *
import time

# >>> Code inspired from professor's slides <<<
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)


# >> Launching server <<
print(">>>Server ready, waiting for client...")
while True:
    connectionSocket, address = serverSocket.accept()
    ping = connectionSocket.recv(2048)
    server_time=time.time() #Getting time from server
    server_time_str=str(server_time) #Converting time to str
    connectionSocket.send(server_time_str.encode("utf-8"))
    connectionSocket.close()