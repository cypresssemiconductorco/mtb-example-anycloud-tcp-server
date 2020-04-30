#******************************************************************************
# File Name:   tcp_client.py
#
# Description: A simple python based TCP client.
# 
#******************************************************************************
# (c) 2019-2020, Cypress Semiconductor Corporation. All rights reserved.
#******************************************************************************
# This software, including source code, documentation and related materials
# ("Software"), is owned by Cypress Semiconductor Corporation or one of its
# subsidiaries ("Cypress") and is protected by and subject to worldwide patent
# protection (United States and foreign), United States copyright laws and
# international treaty provisions. Therefore, you may use this Software only
# as provided in the license agreement accompanying the software package from
# which you obtained this Software ("EULA").
#
# If no EULA applies, Cypress hereby grants you a personal, non-exclusive,
# non-transferable license to copy, modify, and compile the Software source
# code solely for use in connection with Cypress's integrated circuit products.
# Any reproduction, modification, translation, compilation, or representation
# of this Software except as specified above is prohibited without the express
# written permission of Cypress.
#
# Disclaimer: THIS SOFTWARE IS PROVIDED AS-IS, WITH NO WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, NONINFRINGEMENT, IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. Cypress
# reserves the right to make changes to the Software without notice. Cypress
# does not assume any liability arising out of the application or use of the
# Software or any product or circuit described in the Software. Cypress does
# not authorize its products for use in any products where a malfunction or
# failure of the Cypress product may reasonably be expected to result in
# significant property damage, injury or death ("High Risk Product"). By
# including Cypress's product in a High Risk Product, the manufacturer of such
# system or application assumes all risk of such use and in doing so agrees to
# indemnify Cypress against all liability.
#******************************************************************************/

#!/usr/bin/env python
import socket
import optparse
import time
import sys


BUFFER_SIZE = 1024

# IP details for the TCP server
DEFAULT_IP   = '192.168.18.10'   # IP address of the TCP server
DEFAULT_PORT = 50007             # Port of the TCP server

DEFAULT_KEEP_ALIVE = 0           # Keep the connection alive (=1), or close the connection (=0)


def tcp_client( server_ip, server_port, test_keepalive ):
    print("================================================================================")
    print("TCP Client")
    print("================================================================================")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    print("Connected to TCP Server (IP Address: ", DEFAULT_IP, "Port: ", DEFAULT_PORT, " )")
        
    while 1:
        print("================================================================================")        
        data = s.recv(BUFFER_SIZE);
        print("Command from Server:")
        if data.decode('utf-8') == '0':
            print("LED OFF")
            message = 'LED OFF ACK'
            s.send(message.encode('utf-8'))
        if data.decode('utf-8') == '1':
            print("LED ON")
            message = 'LED ON ACK'
            s.send(message.encode('utf-8'))
        print("Acknowledgement sent to server")        
    


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("--hostip", dest="hostip", default=DEFAULT_IP, help="Hostip to listen on.")
    parser.add_option("-p", "--port", dest="port", type="int", default=DEFAULT_PORT, help="Port to listen on [default: %default].")
    parser.add_option("--test_keepalive", dest="test_keepalive", type="int", default=DEFAULT_KEEP_ALIVE, help="Test keepalive capability")
    (options, args) = parser.parse_args()
    #start tcp client
    tcp_client(options.hostip, options.port, options.test_keepalive)

