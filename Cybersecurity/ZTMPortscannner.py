

import socket #commmunicate with tcp/udp packets


#iterate ports from 1 and call scan port function for the port
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):  #calls function using both parameters
	try: #try to inciate socket function
		sock = socket.socket() #calling libray and sock function
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port)) #prints port opened and port number
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print("[*]Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports) #scans one Ip address
