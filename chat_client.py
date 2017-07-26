import socket
import sys #to quit the program

chat_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
host_ip = socket.gethostbyname(host)
port = 1234
chat_client.connect((host_ip,port))

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

chat_client.close()

"""
def send_message():
  while(True):
    message = raw_input("Me : ")
    message = "Client : " + message
    chat_client.sendall(message)
    
    if "bye" in responce.lower():
      sys.exit(0)

def receive_message():
  while(True):
    responce = chat_client.recv(4096)
    print responce

    if "bye" in responce.lower():
      sys.exit(0)
"""