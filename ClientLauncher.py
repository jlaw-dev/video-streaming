import sys, argparse
from tkinter import Tk
from Client import Client

if __name__ == "__main__":
        app = None
        args = None

        try:
                parser = argparse.ArgumentParser(description="Launches RTP Client.")
                parser.add_argument('server_name', help="The name of the server host")
                parser.add_argument('server_port', help="The server port number", type=int)
                parser.add_argument('rtp_port', help="The port receiving RTP packets", type=int)
                parser.add_argument('video_file', help="The name of the video file")
                parser.add_argument('--interface', '-i', action='store_true', help="indicates whether to start client w/ 3-Button interface")

                args = parser.parse_args()

        except:
                print("Unable to parse command line arguments.\n")        
        
        root = Tk()

        # Create a new client
        app = Client(root, args.server_name, args.server_port, args.rtp_port, args.video_file, args.interface)
        app.master.title("RTPClient")   
        root.mainloop()
	
