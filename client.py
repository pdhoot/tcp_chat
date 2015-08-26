import socket , sys , signal
from Node import Node

class Client(Node):

	def __init__(self , host , port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	def start(self , username):
		self.sock.connect((self.host , self.port))
		def signal_handler(signal , frame):
			print "Ok! The client wants to shut down!"
			self.sock.close()
			sys.exit(0)
		while True:
			msg = raw_input()
			signal.signal(signal.SIGINT , signal_handler)
			msg+='\n'
			msg = '<' + username + '>' + msg
			self.sendMsg(self.sock , msg)


if __name__=='__main__':
	client = Client(sys.argv[1] , 1060)
	username = raw_input()
	client.start(username)