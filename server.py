#server.py

#!/usr/bin/env python

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

class ClientThread(Thread):
    
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ip+":"+str(port)
    
    
    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print "received data:", data
            conn.send(data)  # echo

TCP_IP = '0.0.0.0'
TCP_PORT = 9999
BUFFER_SIZE = 1024


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
#connections = []

while True:
    tcpsock.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)
    #connectins.append(conn)

for t in threads:
    t.join()
