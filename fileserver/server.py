import socket
import os
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',5000))
print("Server PID ",os.getpid())
server.listen(5)
def handle_client(conn):
	try:
		filename=conn.recv(1024).decode().strip()
		if os.path.isfile(filename):
			with open(filename,"r") as f:
				data=f.read()
				data=f"{os.getpid()}\n{data}"
				conn.sendall(data.encode())
		else:
			data=f"{os.getpid()}\nfile not found"
			conn.sendall(data.encode())
	except Exception as e:
		print("error handling ",e)
	finally:
		conn.close()
while True:
	conn,addr=server.accept()
	thread=threading.Thread(target=handle_client,args=(conn,))
	
	
	thread.start()
