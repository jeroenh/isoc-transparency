import socket
import sys
import datetime
import logging

SERVER = "host.domain.com"

def sendMessage(port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    logging.info( "Socket timeout is set to %s seconds" % sock.gettimeout())

    server_address = (SERVER, port)
    message = 'This is the message.'

    try:

        # Send data
        logging.info( 'sending "%s" on port %s' % (message, port))
        sent = sock.sendto(message, server_address)

        # Receive response
        logging.info( 'waiting to receive')
        data, server = sock.recvfrom(4096)
        logging.info('received reply for port %s' % port)
    except socket.timeout:
        logging.info("Response timed out after %s seconds" % sock.gettimeout())
        print("Response timed out after %s seconds for port %s" % (sock.gettimeout(),port))
        
    finally:
        logging.info('closing socket')
        sock.close()

if __name__ == '__main__':
    logging.basicConfig(filename='udp-client.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
    
    sendMessage(5061)
    sendMessage(5060)
