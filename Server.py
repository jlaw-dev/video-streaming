import sys, socket, argparse

from ServerWorker import ServerWorker

class Server:	
	
	def main(self):
		args = None

		try:
			parser = argparse.ArgumentParser(description="Launches RTP Server.")
			parser.add_argument('server_port', help="The server port number", type=int)
			parser.add_argument('--packet_loss', '-l', help="The percentage of RTP packets lost", type=int, choices=range(0,100), default=0)
			parser.add_argument('--jitter', '-j', help="The amount of jitter in milliseconds", default=0)

			args = parser.parse_args()
		except:
			print("Unable to parse command line arguments.\n")
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rtspSocket.bind(('', args.server_port))
		rtspSocket.listen(5)        

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept()
			ServerWorker(clientInfo, args.packet_loss, args.jitter).run()

if __name__ == "__main__":
	(Server()).main()


