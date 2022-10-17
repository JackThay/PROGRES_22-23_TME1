'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Client side of ex2 from TME1
'''
from socket import *
import time
import datetime

# >>> Code inspired from professor's slides <<<
serverName = "127.0.0.1"
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

ping = bytes(1)

client_time=time.time()
clientSocket.send(ping)
server_time_bytes = clientSocket.recv(2048) #Receiving bytes from server
server_time_str=server_time_bytes.decode("utf-8") #Converting bytes to str
server_time=float(server_time_str) #Converting str to float
time_difference=server_time-client_time #Calculating time difference between server and client
print(">>Time from client's device :" + str(datetime.datetime.fromtimestamp(client_time))) #Converting client's time to datetime
print(">>Time from server's device :" + str(datetime.datetime.fromtimestamp(server_time))) #Converting server's time to datetime
print(">>Time difference between client and server is :" + str(time_difference)) #Displaying time difference between server and client
print("<!>Time difference doesn't take into account lag between client and server<!>")
clientSocket.close()

'''
(In French)
Exercice 2 - Client / Serveur TCP

1. A partir des exemples de code vus en cours pour le client et le serveur TCP, programmer le
mécanisme de calcul de différence d'horloge entre le client et le serveur en Python ;
>>  Voir code plus haut ainsi que Ex2_server.py

2. Tester les programmes client et serveur sur la même machine et sur des machines différentes ;
>>  Adresse IP utilisé pour les tests sur la même machine : 127.0.0.1 (loopback)
    Adresse IP utilisé pour les tests sur plusieurs machines : 192.168.0.10 (Adresse IP locale sur mon réseau à domicile)
    La différence d'heure est nul lorsque les tests sont réalisés sur la même machine.
    Il existe un très léger décalage lorsque les tests sont réalisés sur des machines différentes.

3. Tester le serveur et plusieurs clients qui sont lancés simultanément.
>>  "screen python3 Ex2_client.py"
    Le serveur a pu répondre à une seul requête parmi les requêtes simultanées de nos clients.
'''