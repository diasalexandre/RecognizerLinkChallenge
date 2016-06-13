#!/usr/bin/python
# -*- coding: iso8859-1 -*-
from socket import *
from sys import argv,exit
import untangle
import re
from array import *

class Product:
     def __init__(self, id, title, price, link):
         self.id = id
         self.title = title
         self.price = price
         self.link = link

def conecta(ip,porta):
    sock = socket(AF_INET,SOCK_STREAM) 
    sock.connect((ip,int(porta))) 
    return sock

def regularLink():
    return "^(https?:\/\/)?(.*)\.([\da-z\.-]+)\.([a-z\.]{2,6})\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"

stores = { }

def server():
    NUMERO_CONEXOES = 700

    if len(argv) < 3:
        exit(1)
        
    sock = socket(AF_INET,SOCK_STREAM)  
    sock.bind(("localhost",int(argv[2])))
    sock.listen(NUMERO_CONEXOES)    
    client = sock.accept()  
    new_sock = client[0]    
    ip = client[1][0] 

    BY = 1024
    try:
        msg = True
        while msg != None:
            msg = new_sock.recv(BY)   
            groupLink = re.match(regularLink(), msg)

            storeName = str(groupLink.group(2))

            if storeName == "www":
                storeName = str(groupLink.group(3));

            found = 0

            if (storeName in stores.keys()):
                for item in stores.get(storeName):
                    if msg == item.link:
                        found = 1
            else: 
                new_sock.sendall("invalid store") 

            if found == 0:
                new_sock.sendall("not found") 
            else:
                new_sock.sendall("found") 

    except KeyboardInterrupt:   
        exit(0)


def createStructure():
    obj = untangle.parse('xmllojas.xml')
    
    for item in obj.xml.item:
        prod = Product(item.id.cdata, item.title.cdata, item.price.cdata, item.link.cdata)
        storeName = item.store.cdata.lower().replace(" ", "");

        if (storeName not in stores.keys()):
            stores[storeName] = []
        
        stores[storeName].append(prod)        

if __name__ == "__main__":
    args = ("-s","-c","-h")
    if len(argv) < 2 or argv[1] not in args or argv[1] == "-h":
        exit(1)
    
    if argv[1] == args[0]:
        createStructure()
        print "Executando o server.\n"
        server()
        
    exit(0)    
