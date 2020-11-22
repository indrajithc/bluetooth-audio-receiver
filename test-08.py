"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

hostMACAddress =  "E4:46:DA:2A:09:F6" # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1


backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.bind(("",bluetooth.PORT_ANY))
# s.listen(1)

# port = s.getsockname()[1]

# print(port)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    print("ff")
    client, clientInfo = s.accept()
    print("ee")
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()