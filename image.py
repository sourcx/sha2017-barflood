import socket
import sys
import os
from scipy import misc


def socket():
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

	return s


def flood(image = 'bier.bmp', off_x = 0, off_y = 0):
	image = misc.imread(os.path.join(image), flatten= 0)

	len_y = len(image)
	len_x = len(image[0])

	pixeldata = ""

	for y in range(len_y):
		for x in range(len_x):
			r, g, b = image[y][x]
			v = "%0.6X" % ((r << 16) + (g << 8) + b)
			pixeldata = pixeldata + "PX {} {} {}\n".format(x + off_x, y + off_y, v)

	s = socket()

	while True:
	    s.sendall(pixeldata)


flood('bier.bmp', 0, 0)
flood('bier.bmp', 240, 0)
# flood('flag.bmp', 320, 0)
# flood('fallout.bmp', 80, 24)
# flood('happyhour.bmp', 100, 24)
