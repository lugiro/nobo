#!/usr/bin/env python3

import socket
import sys

from datetime import datetime

now = datetime.now()                                                   # current date and time
date_time = now.strftime("%Y%m%d%H%M%S")

HOST = "IPadress"                                                      # The server's hostname or IP address
PORT = 27779                                                           # The port used by the server

print ("NOBO API")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:           # Initiate socket
    s.connect((HOST, PORT))
    print ("--HANDSHAKE--")
    handshake_message = "HELLO 1.1 yyyyyyyyyyyy "+ date_time + "\r"    #yyyyyyyyyyyy HUB serial number
    bytemessage = handshake_message.encode()                           #convert from string to byte
    print ("Sent: ",bytemessage)
    s.sendall(bytemessage)                                             #send byte data on socket
    data = s.recv(1024)                                                #returned data
    print("Received: ", repr(data))

    handshake_message = "HANDSHAKE\r"
    bytemessage = handshake_message.encode()                           #convert from string to byte
    print ("Sent: ",bytemessage)
    s.sendall(bytemessage)                                             #send byte data on socket
    data = s.recv(1024)                                                #returned data
    print("Received: ", repr(data))

    print ("--COMMAND--")
    command = "G00\r"                                                  #G00 kommando
    command_byte = command.encode()
    print ("Sent: ",command_byte)
    s.sendall(command_byte)

    print ("--RECEIVED--")
    returnH05 ="000"
    while (returnH05 != "H05"):                                        #check for the last return data
        return_data = s.recv(1024)                                     #returned data
        return_data_str = return_data.decode("utf-8")                  #convert from byte to string
        return_data_str = return_data_str.replace('\r', '')            #remove \r at the end of data line"
        print (return_data_str) 

        return_data_items = return_data_str.split(' ')                 #splitt list items with space
        num_of_items = len(return_data_items)                          #get number of items in list

        if return_data_items[0] == "H05":                              #find the last return data
            returnH05 = "H05" 
