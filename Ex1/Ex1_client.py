'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Client side of ex1 from TME1
'''
from socket import *
import time

# >>> Code inspired from professor's slides <<<
serverName = "127.0.0.1" #Write down here the destination's IP
serverPort = 1234 #Write down here the destination's port
clientSocket = socket(AF_INET,SOCK_DGRAM)

ping = bytes(1)

# >> Sending Ping <<
print(">Sending Ping...")
start_pingtime=time.time()
clientSocket.sendto(ping,(serverName,serverPort))

# >> Recceiving Pong <<
pong, serverAddress = clientSocket.recvfrom(2048)
finish_pingtime=time.time()
print(">Pong received!")

# >> Displaying received message <<
pingtime=finish_pingtime-start_pingtime
print("== Received modified message :" + str(pong.decode("utf-8")) + " ==")
print("== Ping time was :" + str(pingtime) +" ==")
clientSocket.close()

'''
(In French)
Exercice 1 - Client / Serveur UDP

1. A partir des exemples de code vus en cours pour le client et le serveur UDP, programmer le
mécanisme PING client / serveur en Python ;
>>  Voir code plus haut ainsi que Ex1_server.py

2. Tester les programmes client et serveur sur la même machine et sur des machines différentes ;
>>  Adresse IP utilisé pour les tests sur la même machine : 127.0.0.1 (loopback)
    Adresse IP utilisé pour les tests sur plusieurs machines : 192.168.0.10 (Adresse IP locale sur mon réseau à domicile)
    Le code fonctionne dans les 2 cas, le ping prend cependant plus de temps lorsque le serveur et le client sont
    sur des machines différente que lorsque elle sont en loopback.

3. Tester le serveur et plusieurs clients qui effectuent des requêtes simultanées ;
>>  Le serveur a pu répondre aux requêtes simultanées de nos clients.

4. Modifier le code du serveur pour qu'il oublie de répondre avec une probabilité 0.5 à une
requête formulée par un client. Que se passe-t'il ?
>>  Voir code Ex1_server_1-2chance.py
>>  Le client Ex1_client.py attend indéfiniment une réponse de la part du serveur.

Modifier le client pour rétablir un fonctionnement normal. Tester les modifications comme en 2. et 3.
>>  Voir code Ex1_client_1-2chance.py
    2. Le programme fonctionne comme supposé, avec une probabilité de 1/2 qu'il ne réponde pas au ping, 
    aussi bien en loop back que sur des machines différentes.
    3. Le serveur est capable de gérer plusieurs requêtes clients en simultanées, toujours avec une probabilité
    de 1/2 de ne pas répondre.
'''