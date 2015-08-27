import socket , sys , signal
from Node import Node
from threading import Thread
from clint.textui import colored

class Client(Node):

	def __init__(self , host , port , passwd):
		self.host = host
		self.port = port
		self.passwd = passwd + '\n'
		self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	def start(self):
		self.sock.connect((self.host , self.port))
		self.sendMsg(self.sock ,self.passwd)
		message = self.recvMsg(self.sock , '\n')
		if message.replace('\n' , '')!='~q':
			username = raw_input(colored.yellow("Enter your username: "))
			Thread(target=self.sends , args = (username,)).start()
			Thread(target=self.recvs , args=('\n',)).start()
		else:
			sys.exit(0)

	def sends(self , username):
		while True: 
			msg = raw_input()
			# signal.signal(signal.SIGINT , signal_handler)
			print "\033[A                             \033[A"
			print colored.yellow("<me>") , colored.magenta(msg)
			if msg=='~q':
				msg+='\n'
				self.sendMsg(self.sock , msg)
				self.sock.shutdown(socket.SHUT_WR)
				break
			msg+='\n'
			msg = '<' + username + '> ' + msg
			self.sendMsg(self.sock , msg)
	def recvs(self , delimeter):
		while True:
			msg = self.recvMsg(self.sock , delimeter)
			if msg.replace('\n' , '')=='~q':
				# self.sock.shutdown(socket.SHUT_RD)
				self.sock.close()
				break
			msg =  msg.replace('\n' , '')
			ind = msg.index('>')
			print colored.yellow(msg[0:ind+1]) , colored.red(msg[ind+1:])

def main(argv):
	client = Client(argv[0] , 1060 , argv[1])
	client.start()