#!/usr/bin/python

import bluetooth

bd_addr = "24:1F:A0:FE:85:43"

port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
f = open('/home/pi/gps.log','w')
while 1:
      data = sock.recv(1024)
      f.write(str(data))         
      #print (data)
sock.close()


