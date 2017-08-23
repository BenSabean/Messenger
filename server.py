#server.py

#!/usr/bin/env python

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

class ClientThread(Thread):
    
    def __init__(self,ip,port,id):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.id = id # the instance's thread id
        print("[+] New thread started for "+ip+" whith id "+str(id)+":"+str(port))
    
    def isValid(self,parsedStr):
        try:
            self.rcvId = int(parsedStr)
            if(self.rcvId > index-1 or self.rcvId < 0):
                return False
            return True
        except ValueError:
            return False


    def sendMsg(self, parsedStr):
        try:
            connections[self.rcvId].send(str(self.id) + ":" + parsedStr[1])  # echo
        except ValueError:
            conn.send("Server: Could not end message")
    
    
    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print("received data: " + data)
            parsed = data.split(":",1)
            print("send to id " + parsed[0])
            
            if(self.isValid(parsed[0])):
                print("Valid ID")
                self.sendMsg(parsed)
            else:
                print("Invalid string")
                conn.send("Server: Could not send message")
        conn.close()


TCP_IP = '0.0.0.0'  # all ip addresses referencing this server
TCP_PORT = 9999
BUFFER_SIZE = 1024


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))

threads = []
connections = []
index = 0

while True:
    tcpsock.listen(4)
    print "Waiting for incoming connections..."

    (conn, (ip,port)) = tcpsock.accept()
    newthread = ClientThread(ip,port,index)
    newthread.start()
    threads.append(newthread)
    connections.append(conn)
    index += 1

for t in threads:
    t.join()
