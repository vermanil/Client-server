import socket
import threading
import time

host = "127.0.0.1"
port = 0

server = ('127.0.0.1',5000)
lock = threading.Lock()
shutdown = False

def recevi_client(name, sock):
	while not shutdown:
		try:
			lock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print(str(data))
		except:
			pass
		finally:
			lock.release()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

thread = threading.Thread(target=recevi_client, args = ("recvThread",s))
thread.start()

user = input("Name : ")
message = input(user + "-->")

while message != 'q':
	if message != "":
		s.sendto(bytes(user + ": " + message,"UTF-8"), server)
		lock.acquire()
		message = input(user + "-->")
		lock.release()
		time.sleep(0.2)
shutdown = True
thread.join()
s.close


