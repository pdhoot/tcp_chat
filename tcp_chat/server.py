import socket, sys , signal
from threading import Thread
from Node import Node


class Server(Node):

	def __init__(self , host , port , passwd):
		self.host = host
		self.port = port
		self.passwd = passwd
		self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
		self.registered_clients = []

	def start(self):
		self.sock.bind((self.host , self.port))
		self.sock.listen(3)
		def chat(sc):		
			while True:
				message = self.recvMsg(sc , '\n')
				if not message:
					break
				if message.replace('\n' , '')=='~q':
					self.sendMsg(sc , message)
					break
				print message.replace('\n' , '')
				self.sendToAllClients(message , sc)
				#Later will have to add a method to escape \n in case it is already present in the message.
			self.deregisterClient(sc)
			sc.close()
		while True:
			sc , peeraddr = self.sock.accept()
			msg = self.recvMsg(sc , '\n')
			if msg.replace('\n' , '') == self.passwd:
				self.sendMsg(sc , 'q\n')
				self.registerClient(sc)
				Thread(target=chat , args=(sc,)).start()
			else:
				self.sendMsg(sc , '~q\n')
				sc.close()

	def registerClient(self , sc):
		if sc not in self.registered_clients:
			self.registered_clients.append(sc)

	def sendToAllClients(self , msg , sc):
		for sock in self.registered_clients:
			if sock is not sc:
				sock.sendall(msg)

	def deregisterClient(self , sc):
		if sc in self.registered_clients:
			self.registered_clients.remove(sc)

def main(argv):
	server = Server(argv[0] , 1060 , argv[1])
	try:
		server.start()
	except KeyboardInterrupt:
		print "Ok! stopping the server!"
		sys.exit(0)