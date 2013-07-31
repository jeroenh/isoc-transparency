import socket
import sys
import logging

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print "Please provide a port number as first argument"
    sys.exit()

port = int(sys.argv[1])
logging.basicConfig(filename='udp-server.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('positron.dckd.nl', port)
logging.info('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    logging.info('waiting to receive message')
    data, address = sock.recvfrom(4096)
    
    logging.info('received %s bytes from %s on %s' % (len(data), address, port))
    logging.info('\t %s' % data)
    
    if data:
        sent = sock.sendto(data, address)
        logging.info('sent %s bytes back to %s' % (sent, address))

