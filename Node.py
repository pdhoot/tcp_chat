class Node(object):
	
	def sendMsg(self , sock , message):
		sock.sendall(message)

	def recvMsg(self, sock , delimeter):
		message = ""
		while True:
			data = sock.recv(4096)
			if not data:
				break
			message+=data
			if delimeter in data:
				break
		return message