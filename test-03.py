import bluetooth

name="bt_server"
target_name="Redmi"
uuid="00001105-0000-1000-8000-00805f9b34fb"

def runServer():
    serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    port=bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print ("Listening for connections on port: ", port   )

    # wait for a message to be sent to this socket only once
    serverSocket.listen(1)
    port=serverSocket.getsockname()[1]

    # you were 90% there, just needed to use the pyBluez command:
    bluetooth.advertise_service( serverSocket, "SampleServer",
                        service_id = uuid,
                        service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                        profiles = [ bluetooth.SERIAL_PORT_PROFILE ] 
                        )

    inputSocket, address=serverSocket.accept()
    print ("Got connection with" , address)
    data=inputSocket.recv(1024)
    print ("received [%s] \n " % data   ) 
    inputSocket.close()
    serverSocket.close()  

runServer()  