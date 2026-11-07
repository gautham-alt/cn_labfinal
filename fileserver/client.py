import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5000))
filename=input("Enter filename")
client.send(filename.encode())
while True:
	chunk=client.recv(4096)
	if not chunk:
		break
	print(chunk.decode(),end="")
print()
client.close()
