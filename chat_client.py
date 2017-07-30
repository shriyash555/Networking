import socket
import thread #for multithreading

def send_message():
  while(True):
    message = raw_input("Me : ")
    message = "Client : " + message
    chat_client.sendall(message)
    
    if "bye" in responce.lower():
      exit()

def receive_message():
  while(True):
    responce = chat_client.recv(4096)
    print responce

    if "bye" in responce.lower():
      exit()

chat_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
host_ip = socket.gethostbyname(host)
port = 1234
chat_client.connect((host_ip,port))

try:
  thread.start_new_thread(send_message, ())
  thread.start_new_thread(receive_message, ())
except Exception,msg:
  print "something bad happen to client that says"
  print msg

"""
#This is the code I have written in the first place

while(True):
  #TODO client thread no. 1 will handle sending of message from client to server
  message = raw_input("Me : ")
  message = "Client : " + message
  chat_client.sendall(message)

  if "bye" in message.lower():
    break

  #TODO client thread no. 2 will handle receiving message from server.
  responce = chat_client.recv(4096)
  print responce

  if "bye" in responce.lower():
    break

chat_client.close()"""

