## page 32
import socket
print "start:"
print "Waiting for data from Client..."

##creating server ##
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 1729))
server_socket.listen(2)
(client_socket, client_address) = server_socket.accept()
client_data = client_socket.recv(1024)
print "data the client sent:" + client_data
print "Client-Data = " +  str( tuple(client_address) )
print "Sending to client the following msg: connected to server, data sent to server -" + client_data
client_socket.send("connected to server, data sent to server - " + client_data)

flag = 0
while flag == 0:
 print "keep session (y/n)?" 
 ans = raw_input()
 if ans == 'y' :
   print "Waiting for data from Client..."
   server_socket.listen(2)
   (client_socket, client_address) = server_socket.accept()
   client_data = client_socket.recv(1024)
   print "data the client sent:" + client_data
   print "Client-Data = " +  str( tuple(client_address) )
   print "Sending to client the following msg: connected to server, data sent to server -" + client_data
   client_socket.send("connected to server, data sent to server - " + client_data)
 else:
  flag = 1
  client_socket.close()
#here we choose to end the session with the client and can connect another client#

server_socket.close()


## serverrr
