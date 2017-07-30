import socket
import thread

def receive_message():
  while(True):
    message = conn.recv(4096)
    print message

    if "bye" in message.lower():
      exit()

def send_message():
  responce = raw_input("Me : ")
  responce = "Server : " + responce
  conn.sendall(responce)

  if "bye" in responce.lower():
    exit()

chat_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
host_ip = socket.gethostbyname(host)
port = 1234
chat_server.bind((host_ip,port))
chat_server.listen(1)
conn , addr = chat_server.accept()

try:
  thread.start_new_thread(receive_message, ())
  thread.start_new_thread(send_message, ())
except Exception,msg:
  print "something bad happen to server that says"
  print mgs

"""
while(True):

  #TODO server thread no. 1 will handle receiving message from client.
  message = conn.recv(4096)
  print message

  if "bye" in message.lower():
    break

  #TODO server thread no.2 will handle sending message from server to client.
  responce = raw_input("Me : ")
  responce = "Server : " + responce
  conn.sendall(responce)

  if "bye" in responce.lower():
    break

chat_server.close()"""

