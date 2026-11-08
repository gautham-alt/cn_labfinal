import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
a={
"cs1":["gautham",99,100],
"cs2":["gau",100,200]
}
ip=("127.0.0.1",5000)
server.bind(ip)
server.listen(5)
sum=0
def handle(conn,addr):
	data=conn.recv(1024).decode()
	sum=0
	if data in a.keys():
		x=a[data]
		m=0
		for i in x:
			if m==0:
				m+=1
				continue
			sum+=i
		sum=f"{a[data][0]} : {sum} : {sum/2}"
		conn.send(sum.encode())
		ack=conn.recv(1024)
		
	else:
		conn.send("student not found".encode())
		ack=conn.recv(1024)
	conn.send(str(a).encode())
	conn.close()
while True:
	conn,addr=server.accept()
	thread=threading.Thread(target=handle,args=(conn,addr),daemon=True)
	thread.start()
	
