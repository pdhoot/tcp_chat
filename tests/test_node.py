import socket
from tcp_chat.Node import Node
import unittest

class NodeTest(unittest.TestCase):

	def test_send_recv(self):
		s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s1.bind(('localhost' , 6969))
		s1.listen(3)
		msg = "This is a very long message, deliberately created to test the sendall and the receive function of the Node class"
		delimeter = "~q"
		s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s2.connect(('localhost', 6969))
		n = Node()
		n.sendMsg(s2 , msg+delimeter)
		sc , peeraddr = s1.accept()
		message = n.recvMsg(sc , delimeter)
		assert message==msg+delimeter