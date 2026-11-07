import socket 
import threading
from datetime import datetime

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.2",5000))
print("time server running")
def handle_client(data,addr,server):
	print("request recvied from ",addr)
	cur=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	server.sendto(cur.encode(),addr)
	print("time sent to  ",addr)
while True:
	data,addr=server.recvfrom(1024)
	thread=threading.Thread(target=handle_client,args=(data,addr,server))
	thread.start()
