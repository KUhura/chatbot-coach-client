import socket #communicate  over network
from threading import Thread #(managed by os)allows me to do multiple things at onece
import sys
import telnetlib

IP= '0.0.0.0'#no specific IP adress
port= 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
#accessing socket library and method
#send perameter using IP v 4
#TCP connection


class Server:
  """allows multiple people to connect , send a messsage and recive it
  back and be notified when someone is connected and disconected """
  links = []
  def __init__(self):
      """"it's a function known as the Instantiation Method.
      it initialises objects of a class."""
      self.s.bind((IP, port))
      self.s.listen(5)#reieve 5 connections at a time
  print ('Socket bind complete')
  print ('Socket now listening')

    #l=list a=address
  def ServerManager(self, l, a):
    """accepts variable l and a (address) as a parameter"""
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
        """accepts a single parameter self which represents the particular object being created. """
        while True:# manages connections 
            l, a = self.sock.accept()#return connection and address of client, accept connection
            input_Thread = threading.Thread(target=self.ServerManager, args=(l,a))#accessing threading method
            input_Thread.daemon = True#program can exit reguardless is a thread is still running 
            input_Thread.start()#starts thread
            self.links.extend(l)
            print(str(a[0]) + 't' + str(a[1]), "a client has been connected")import socket #communicate  over network
from threading import Thread #(managed by os)allows me to do multiple things at onece
import sys
import telnetlib

IP= '0.0.0.0'#no specific IP adress
port= 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
#accessing socket library and method
#send perameter using IP v 4
#TCP connection


class Server:
  """allows multiple people to connect , send a messsage and recive it
  back and be notified when someone is connected and disconected """
  links = []
  def __init__(self):
      """"it's a function known as the Instantiation Method.
      it initialises objects of a class."""
      self.s.bind((IP, port))
      self.s.listen(5)#reieve 5 connections at a time
  print ('Socket bind complete')
  print ('Socket now listening')

    #l=list a=address
  def ServerManager(self, l, a):
    """accepts variable l and a (address) as a parameter"""
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
        """accepts a single parameter self which represents the particular object being created. """
        while True:# manages connections 
            l, a = self.sock.accept()#return connection and address of client, accept connection
            input_Thread = threading.Thread(target=self.ServerManager, args=(l,a))#accessing threading method
            input_Thread.daemon = True#program can exit reguardless is a thread is still running 
            input_Thread.start()#starts thread
            self.links.extend(l)
            print(str(a[0]) + 't' + str(a[1]), "a client has been connected")
