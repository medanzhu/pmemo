import fnmatch
import os
import socket
import sys


rootPath = 'D:/github/iwall_test/testcases'
pattern = '*.case'
PORT = 80
HOST = 'www.tcxa.com.cn'


def read_payload(filename):
	payload_file = os.path.join(root, filename).replace('/','\\')
	with open(payload_file, 'rb') as f:
		payload = f.read()
		return payload;
	
def send_socket(payload):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (HOST, PORT)
		sock.connect(server_address)
		sock.sendall(payload)
		data = sock.recv(1024)
		print(data)

	except:
		sock.close()
		sock = None
		e = sys.exc_info()[0]
		print("Handling run-time error: %s "  % e)
        
	
	
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
		payload = read_payload(filename)
		print(payload)
		send_socket(payload)