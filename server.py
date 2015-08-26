import socket, sys
from threading import Thread
from Node import Node

class Server(Node):

	def __init__(self , host , port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

	def start(self):
		self.sock.bind((self.host , self.port))
		self.sock.listen(3)
		def chat(sc):		
			while True:
				message = self.recvMsg(sc , '\n')
				if not message:
					break
				print message.replace('\n' , '')
				#Later will have to add a method to escape \n in case it is already present in the message.
			sc.close()
		while True:
			sc , peeraddr = self.sock.accept()
			Thread(target=chat , args=(sc,)).start()

	def registerClient(self):
		print "Hello"
		#This is basically to register all the clients
		#that will be receiving any message sent to the server
		#basically these are the clients registered on the server

if __name__=='__main__':
	server = Server(sys.argv[1] , 1060)
	server.start()