import argparse
import server 
import client

def main():
	desc = "A chat app built over TCP"
	parser = argparse.ArgumentParser(description = desc)
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-s' , '--server' , action='store_true' , help = 'starts the server')
	group.add_argument('-c' , '--client' , action='store_true' , help = 'starts the client')
	parser.add_argument('interface')
	parser.add_argument('password')
	args = parser.parse_args()
	argv = [args.interface , args.password]

	if args.server== True:
		server.main(argv)
	elif args.client== True:
		client.main(argv)
	else:
		parser.print_help()