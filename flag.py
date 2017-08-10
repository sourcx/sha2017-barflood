# Echo client program
import socket
import sys
import os

def small():
	pixeldata = ""

	for x in range(80, 320):
	    for y in range(24, 80):
			pixeldata = pixeldata + "PX {} {} CC0000\n".format(x , y)
	for x in range(80, 320):
	    for y in range(80, 150):
			pixeldata = pixeldata + "PX {} {} FFFFFF\n".format(x , y)
	for x in range(80, 320):
	    for y in range(150, 320):
			pixeldata = pixeldata + "PX {} {} 0000CC\n".format(x , y)

  return pixeldata


def large():
	pixeldata = ""

	for x in range(400, 480):
	    for y in range(0, 26):
	    	pixeldata = pixeldata + "PX " + str(x) + " " + str(y) + " FF0000\n"
	for x in range(400, 480):
	    for y in range(27, 54):
	    	pixeldata = pixeldata + "PX " + str(x) + " " + str(y) + " FFFFFF\n"
	for x in range(400, 480):
	    for y in range(55, 80):
	    	pixeldata = pixeldata + "PX " + str(x) + " " + str(y) + " 0000FF\n"

  return pixeldata


def showflag():
	HOST = 'barflood.sha2017.org'
	PORT = 2342
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
	    af, socktype, proto, canonname, sa = res
	    try:
	        s = socket.socket(af, socktype, proto)
	    except socket.error as msg:
	        s = None
	        continue
	    try:
	        s.connect(sa)
	    except socket.error as msg:
	        s.close()
	        s = None
	        continue
	    break
	if s is None:
	    print 'could not open socket'
	    sys.exit(1)

  pixeldata = small()
  # pixeldata = large()

	while True:
	    s.sendall(pixeldata)


showflag()

