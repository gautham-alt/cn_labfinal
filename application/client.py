import socket
import ast
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5000))
n=input("Enter roll no ")
client.send(n.encode())
data=client.recv(1024)
client.send("done".encode())
a=client.recv(1024)
print(data.decode())
print(ast.literal_eval(a.decode()))
client.close()
