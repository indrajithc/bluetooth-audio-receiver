
import bluetooth


addr = "E4:46:DA:2A:09:F6"
bd_addr = addr

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()