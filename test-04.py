"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

hostMACAddress = 'E4:46:DA:2A:09:F6' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM) 
s.bind((hostMACAddress, port)) 
s.listen(backlog) 
try:
    print(s)
    client, clientInfo = s.accept()
    print("da")
    while 1:
        print("loop")
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()