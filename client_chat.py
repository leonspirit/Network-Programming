import sys
import socket
import select
 
def chat_client():

	sys.stdout.write('Host : ')
	host = sys.stdin.readline()
	
	sys.stdout.write('Port : ')
	port = int(sys.stdin.readline())
     
    # create TCP/IP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.settimeout(2)
     
    # connect to remote host
	try :
		s.connect((host, port))
	except :
		print 'Client is unable to connect'
		sys.exit()
     
	print 'Client is now connected to remote host. You can start sending messages'
	sys.stdout.write('>> '); sys.stdout.flush()
     
	while 1:
		socket_list = [sys.stdin, s]
		 
		# Get the list sockets which are readable
		ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
		 
		for sock in ready_to_read:             
			if sock == s:
				# incoming message from remote server, s
				data = sock.recv(4096)
				if not data :
					print '\nYou are disconnected from chat server'
					sys.exit()
				else :
					#print data
					sys.stdout.write(data)
					sys.stdout.write('>> '); sys.stdout.flush()     
			
			else :
				# user entered a message
				msg = sys.stdin.readline()
				s.send(msg)
				sys.stdout.write('>> '); sys.stdout.flush() 


chat_client()
