import socket
print "start:"

##open socket, send and recieve data, close socket ##
user_socket = socket.socket()
user_socket.connect(('127.0.0.1', 1729))
print 'please enter message to server'
user_input = raw_input()
user_socket.send(user_input)
data = user_socket.recv(1024)
print data
flag = 0
while flag == 0:
  print "keep session with SERVER (y/n)?" 
  ans = raw_input()
  if ans == 'y':
   print "Please enter another msg..."
   user_input = raw_input()
   user_socket.send(user_input)
   data = user_socket.recv(1024)
  else :
   flag = 1
   user_socket.close()




