#client.py

#!/usr/bin/env python

import socket
from threading import Thread
#from SocketServer import ThreadingMixIn

class ListenerThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        while True:
            reply = s.recv(2048)
            print(reply)


TCP_IP = '127.0.0.1'  # localhost address
TCP_PORT = 9999
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

threads = []
Listener = ListenerThread()
Listener.start()
threads.append(Listener)

while 1:
    data = raw_input(':> ')
    if data == "self:close": break
    if not data: break
    s.send(data)  # echo

for t in threads:
    t.join()

