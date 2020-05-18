#########################################################
# Name: Jason Marxsen
# Date: 4/24/2020
# Description: Chat (timing) covert channel reader (Python 2)
#########################################################

import socket
import sys
from time import time
from binascii import unhexlify

ZERO = 0.025
ONE = 0.1
DEBUG = False

ip = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

covert_binary = ""
data = s.recv(4096)

while((data.rstrip("\n")).encode() != "EOF"):
	sys.stdout.write(data)
	sys.stdout.flush()

	t0=time()
	data = s.recv(4096)
	t1=time()
	datatime = round(t1-t0, 3)
	if(datatime>=ONE):
		covert_binary+="1"
	else:
		covert_binary+="0"
	if(DEBUG == True):		
		sys.stdout.write("{} \n".format(datatime))
		sys.stdout.flush()

s.close()

covert = ""
i = 0
while (i < len(covert_binary)):
	b = covert_binary[i:i+8]
	n = int("0b{}".format(b), 2)
	try:
		obj = (unhexlify("{0:x}".format(n)))
		covert+= obj
	except TypeError:
		covert+="?"
	if(covert[-3:]=="EOF"):
		covert = covert[:-3]
		break;
	i+=8

print("\nCovert Message: "+covert)
