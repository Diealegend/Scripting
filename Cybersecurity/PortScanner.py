#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#The socket.AFINET clariifies the use of IPv4 and socket.Sock_Stream clarifies the type of connection this being TCP
s.settimeout(5) #This line of code is a the set time out of the code


host = input("Please enter IP address:") #HOST is our target machine varible the INPUT allows user input but this could be turned into a static varible.User Input allows better functionality.
port = int(input("Please enter the port you want to scan:")) #Port scan a port that is desired

def portScanner(port):   #this function will go through a if/else staement and output whether the port is open or not.
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)