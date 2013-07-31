ISOC Transparency testing toolkit
---------------------------------

The following scripts have been used to prove that some providers in the Netherlands block port 5060.
To test this for yourself you can use this code.

Usage Instructions
==================

- Grab a host that is publicly reachable on the internet and download this code
- Grab a laptop and phone and setup a bluetooth tethering connection, or Wifi sharing.
- Edit `udp-client.py` to fill in the address of the server
- On the server: Start two sessions, preferrably using screen and start the server with `python udp-server.py 5060` and `python udp-server.py 5061`
- On the client: Run `python udp-client.py`
- Compare the udp-client.log on the client with the udp-server.log on the server to see the outcome.

(Depending on your connection you can increase the timeout to make sure that this is not a factor. The argument to the timeout is in seconds, 1 second is 1000 ms)