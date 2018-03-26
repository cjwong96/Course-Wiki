# server.py

import socket                  

port = 5000
host = '192.168.1.116'                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               
s.bind((host, port))           
s.listen(5)                     
filename="1.png"

print ('Server listening....')

while True:
	conn, addr = s.accept()     
	print ('Got connection from'), addr
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
		conn.send(l)
		l = f.read(1024)
	f.close()
	print('Done sending')
	
	conn.close()

	break
	
s.close()
	
