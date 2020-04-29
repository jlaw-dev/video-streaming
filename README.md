# video-streaming
A video streaming Client Server application using RTP/RTSP

To run, start the server with the command
py -3 Server.py server_port packet_loss jitter
whre server_port is the port the server listens to for incoming RTSP, packet_loss is the packet loss percent
and jitter is the ammount of jitter in milliseconds.

Start the client with the command
py -3 ClientLauncher.py server_host server_port RTP_port video_file -4
where server_host is the name of the server, server_port is the port where the server listens on,
RTP_port is the port where RTP packets are recieved and video_file is the name of the video file.
