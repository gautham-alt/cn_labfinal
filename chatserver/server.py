import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",4000))
server.listen(10)
clients=[]
print("server started")
def handle_client(conn,addr):
	while True:
		try:
			data=conn.recv(1024)
			print(addr,' : ',data.decode())
			for i in clients:
				if i!=conn:
					i.send(data)
			if data.decode()=="exit":
				break
		except:
			break
	clients.remove(conn)
	conn.close()
	print("disconnected ",addr)
while True:
	conn,addr=server.accept()
	clients.append(conn)
	print("\n",addr,"joined the chat \n")
	thread=threading.Thread(target=handle_client,args=(conn,addr))
	thread.start()
