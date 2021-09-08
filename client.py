#!/usr/bin/python
#-*-coding:utf-8 -*-

import socket
import cv2
import numpy
import struct

#端口
PORT = 12340
#服务器地址
HOST = socket.gethostname()


#客户端传输函数
def tcp_client(port,cap):
	
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# 连接服务端	
	address_server = (HOST, 12340)
	sock.connect(address_server)
	#读取视频流
	ret, frame = cap.read()
	#图片编码参数
	encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
	while ret:
		#图像编码
		result, imgencode = cv2.imencode('.jpg', frame)
		data = numpy.array(imgencode)
		stringData = data.tobytes()
		#打包传输图像长度
		len_byte = struct.pack('i',len(stringData))
		#传输长度
		sock.send(len_byte)
		#传输图像
		sock.send(stringData)
		#读取视频流
		ret, frame = cap.read()

	cap.release()
	cv2.destroyAllWindows()


def main():
	#设定视频流
	cap = cv2.VideoCapture(0)
	#客户端传输函数
	tcp_client(PORT,cap)

if __name__ == '__main__':
	main()