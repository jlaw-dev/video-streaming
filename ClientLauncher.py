import sys
from tkinter import Tk
from Client import Client

if __name__ == "__main__":
        app = None
        try:
                serverAddr = sys.argv[1]
                serverPort = sys.argv[2]
                rtpPort = sys.argv[3]
                fileName = sys.argv[4]
                has3ButtonInterface = bool(sys.argv[5])
        except:
                print("[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file Has_3_button_interface]\n")        
        
        root = Tk()

        # Create a new client
        app = Client(root,serverAddr,serverPort,rtpPort,fileName,has3ButtonInterface)
        app.master.title("RTPClient")   
        root.mainloop()
	
