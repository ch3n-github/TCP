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
    print ('Port'+str(port)+' is waiting for input...')
    #阻断等待连接
    conn, addr = s.accept()
    #缓存
    time.sleep(2)
    print ('Port'+str(port)+' is connected')

    while 1:
        try:
            #接收图像长度
            head = conn.recv(4)
            if head:
                length = struct.unpack('i',head)[0]
            else:
                break
            #根据图像大小接收图像信息
            stringData = conn.recv(int(length))
            #图像解码
            data = numpy.frombuffer(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,1)
            #图像显示
            cv2.imshow(str(port),decimg)
            #设置中断
            if cv2.waitKey(1) == 27:
                break
        except:
            pass

    print ('Port'+str(port)+' is disconnect')

    s.close()
    


def main():
    tcp_server(PORT)
if __name__ == '__main__':
    main()
