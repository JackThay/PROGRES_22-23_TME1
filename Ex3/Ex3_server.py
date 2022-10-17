'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Server side of ex3 from TME1
'''
from socket import *
import http.server
import socketserver

# >>> Code inspired from https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/ <<<

PORT = 80 #Port 80 because is the standard one for http

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()

'''
(In French)
Exercice 3 - Serveur Web avec TCP

1. Programmer le serveur Web en Python ;
>>  Voir code plus haut

*Remarque:*
- Pour les questions suivantes, les ordinateurs de l'université ne nous permettent pas d'avoir
  les droits pour executer le serveur (autorisation socketserver.py)

2. Tester le programme avec un navigateur Web, sur la même machine et sur des machines
différentes ;
>>  Adresse IP utilisé pour les tests sur la même machine : 127.0.0.1 (loopback)
    Adresse IP utilisé pour les tests sur plusieurs machines : 192.168.0.10 (Adresse IP locale sur mon réseau à domicile)
    Dans les 2 cas, les tests fonctionnent.

3. Tester le serveur et plusieurs clients qui effectuent des requêtes simultanées.
'''