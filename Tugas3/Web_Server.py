import sys
import socket
import time

REQ_SIZE = 10
RECV_BUFFER_SIZE = 1024
message = "<html><body><i>Hello <b>World!</b> </i> <br> <u>Ari here</u> </body> </html>"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sys.stdout.write('Port : ')
PORT = raw_input()
PORT = int (PORT)

# Bind the socket to the port
server_address = ('localhost', PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(REQ_SIZE)

while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()
	print >>sys.stderr, 'Connection from', client_address
	print ''
	request = connection.recv(RECV_BUFFER_SIZE)
	data = "HTTP/1.1 200 OK\n\n%s"%message
	print (request.decode())
	connection.send(data)
	
	# Clean up the connection
	connection.close()
