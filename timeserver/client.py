import socket 
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=("127.0.0.2",5000)
msg="time"
client.sendto(msg.encode(),server_address)
data,addr=client.recvfrom(1024)
print("time is ",data.decode())
client.close()
