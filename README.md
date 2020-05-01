# Video Streaming Application
## A client-server application that uses RTP/RTSP protocol to stream a video file, as well as simualates jitter and packet-loss and calculates statistics about the process
### Running the application
To run, start the server with the command

`py -3 Server.py server_port packet_loss jitter`
- `server_port`: the port the server listens to for incoming RTSP (greater than 1024)
- `packet_loss`: the percentage of packets dropped by the server during transmission
- `jitter`: the amount of jitter in milliseconds


Start the client with the command

`py -3 ClientLauncher.py server_host server_port RTP_port video_file Has_3_button_interface`
- `server_host`: the name of the server
- `server_port`: the port where the server is listening
- `RTP_port`: the port where RTP packets are received
- `video_file`: the name of the video file
- `Has_3_button_interface`: (`true`/`false`) whether to initialize GUI with 3-Button interface
