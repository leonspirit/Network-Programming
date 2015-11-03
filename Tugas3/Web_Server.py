import threading
import socket
import time
import sys

def load_file(name):
	data = open(name)
	return data.read()

class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)
	
	def run(self):
		message = ''
		while True:
        		data = self.client_socket.recv(32)
            		if data:
						message = message + data #collect seluruh data yang diterima
						if message.endswith('\r\n\r\n'):
							self.client_socket.send('hola')
							break
            		else:
               			break
		self.client_socket.close()
		


class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sys.stdout.write('Port : ')
		port = raw_input()
		port = int (port)
		self.server_address = ('localhost',port)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
			nomor=nomor+1
			
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			#----

serverku = Server()
serverku.start()


