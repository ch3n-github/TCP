#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import cv2
import numpy
import struct
import time
from threading import Thread

PORT = 12340

def tcp_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""

    address = (host, port)
    s.bind(address) 
    s.listen(5)
    print ('Waiting for input...')
    conn, addr = s.accept()
    time.sleep(2)


    while 1:
        try:
            head = conn.recv(4)
            if head:
                length = struct.unpack('i',head)[0]
            else:
                break

            stringData = conn.recv(int(length))
            data = numpy.frombuffer(stringData, dtype='uint8')

            decimg=cv2.imdecode(data,1)

            cv2.imshow('SERVER',decimg)
            if cv2.waitKey(10) == 27:
                break
        except:
            pass
    s.close()
    cv2.destroyAllWindows()


def main():
    tcp_server(PORT)
if __name__ == '__main__':
    main()
