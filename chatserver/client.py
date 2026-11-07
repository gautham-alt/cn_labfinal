import socket
import threading
client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",4000))
print("connected to server")
def recv_msg():
	while True:
		try:
			data=client.recv(1024)
			if not data:
				break
			print("\nreceivied : ",data.decode())
			
			if data.decode()=="exit":
				break
			print("You :",end="",flush=True)
				
		except:
			break
thread=threading.Thread(target=recv_msg)
thread.start()
while True:
	msg=input("you :")
	
	client.sendall(msg.encode())
	if msg=="exit":
		break
	
client.close()
