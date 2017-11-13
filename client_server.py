import socket #communicate  over network
from threading import Thread #(managed by os)allows me to do multiple things at onece
import sys

IP= '127.0.0.1'
port= 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#accessing socket library and method
#send perameter using IP v 4
#TCP connection


class Server:


    links = []
    def __init__(self):
        self.s.bind((IP, port))
        self.s.listen(5)#reieve 5 connections at a time

  #l=list a=address
    def ServerManager(self, l, a):
    '''accepts variable l and a (address) as a parameter'''
    global links    
        while true:
            message = l.recv(1024)#max data recived, loop won't run till data recived, message input for user
            for link in links:#sends back data to users
                link.send(message)
            if not message:
                print(str(a[0]) + 't' + str(a[1]), "a client has been disconnected")
                self.connections.remove(l)
                l.close()
            break
            
    def run(self):
        '''takes one argument which is..... of data type....the output is the same data type......'''
        while True:# manages connections 
            l, a = self.sock.accept()#return connection and address of client, accept connection
            input_Thread = threading.Thread(target=self.ServerManager, args=(l,a))#accessing threading method
            input_Thread.daemon = True#program can exit reguardless is a thread is still running 
            input_Thread.start()#starts thread
            self.links.extend(l)
            print(str(a[0]) + 't' + str(a[1]), "a client has been connected")

    

class Client: 
    def sendTxt(self):
    #''' takes in parameter of data type...outputs data type...'''
          self.s.send(bytes(input(""), 'utf-8'))

    def __init__(self):
        self.s.connect((bind, port))
        #''' Takes a tuple'''
        iThread = threading.Thread(target=self.sendTxt)              
        iThread.daemon = True  
        iThread.start()
        while True:
            message = self.sock.recv(1024)#max data that can be recived
            if not message:
                break
                print(str(message, 'utf-8'))
                     
    

if (len(sys.argv)) > 1:#deciding to be client or server
  client = Client(sys.argv[1])
else:
  server = server()
  server.run()