import threading
import socket
import time
import string
import sys

FILE_NAME = ['ted.jpg','banana.gif','petrik.gif','dumb.gif','dolan.jpg','cj7.gif','doge.jpg','husky.jpg','martabak.jpg','mine.jpg']

def load_file(name):
	data = open(name,"r")
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
							data_to_send='HTTP/1.1 200 OK\r\n\r\n'
							
							split_msg = string.split(message[:-1])
							
							#print message
							#print split_msg[1]
							
							if split_msg[1]=='/':
								data_to_send=data_to_send+'<html><body>'
								for x in range(10):
									y = x+1
									data_to_send=data_to_send+'<img src=http://localhost:5252/foto'+str(y)+' /><br>';
									#data_to_send = data_to_send + str(x)
							else:
								photo_numb = split_msg[1][5:]
								photo_numb = int (photo_numb)
								photo_numb = photo_numb - 1
								
								if photo_numb>=10 or photo_numb<0:
									photo_numb=0
								
								data_to_send = data_to_send + load_file(FILE_NAME[photo_numb])
							self.client_socket.send(data_to_send)
							break
            		else:
               			break
		self.client_socket.close()
		


class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sys.stdout.write('Port : ')
		port = raw_input()
		port = int (port)
		self.server_address = ('localhost',port)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while True:
			self.client_socket, self.client_address = self.my_socket.accept()
			nomor=nomor+1
			
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.daemon = True
			my_client.start()
			#----
		self.my_socket.close()


serverku = Server()
serverku.daemon = True
serverku.start()
while True:
	time.sleep(1)
