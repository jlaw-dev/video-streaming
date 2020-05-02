# Video Streaming Application
## A client-server application that uses RTP/RTSP protocol to stream a video file, as well as simualates jitter and packet loss and calculates statistics about the process
### Running the application
To run, start the server with the command:

  Usage:
    `Server.py [--help] [--packet_loss LOSS] [--jitter JITTER] server_port packet_loss jitter`
- Positional arguments
  - `server_port`: the port the server listens to for incoming RTSP (greater than 1024)
- Optional arguemnts
  - `--packet_loss`, `-l`: the percentage of packets dropped by the server during transmission
  - `--jitter`, `-j`: the amount of jitter in milliseconds


Start the client with the command:

  Usage: 
    `ClientLauncher.py [--help] [--interface] server_name server_port RTP_port video_file`
  
- Positional arguments
  - `server_host`: the name of the server
  - `server_port`: the port where the server is listening
  - `RTP_port`: the port where RTP packets are received
  - `video_file`: the name of the video file
- Optional arguments
  - `--help`,`-h`: show this help message and exit
  - `--interface`, `-i`: indicates whether to start client w/ 3-Button interface
