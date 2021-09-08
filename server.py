#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import cv2
import numpy
import struct
import time
from threading import Thread
#端口
PORT = 12340
#服务端接收函数
def tcp_server(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #服务端地址端口设定
    host = ""
    address = (host, port)
    #绑定地址
    s.bind(address) 
    #多线程监听
    s.listen(5)
    print ('Waiting for input...')
    #阻断等待连接
    conn, addr = s.accept()
    #缓存
    time.sleep(2)

    while 1:
        try:
            #接收图像长度
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
