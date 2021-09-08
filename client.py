#!/usr/bin/python
#-*-coding:utf-8 -*-

import socket
import cv2
import numpy
import struct


PORT = 12340
HOST = socket.gethostname()



def tcp_client(port,cap):
	
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# 连接服务端

	
	address_server = (HOST, 12340)
	sock.connect(address_server)
	ret, frame = cap.read()
	encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
	while ret:

		result, imgencode = cv2.imencode('.jpg', frame)
		data = numpy.array(imgencode)
		stringData = data.tobytes()

		len_byte = struct.pack('i',len(stringData))
		sock.send(len_byte)
		sock.send(stringData)
		ret, frame = cap.read()


	cap.release()
	cv2.destroyAllWindows()




def main():
	cap = cv2.VideoCapture(0)

	tcp_client(PORT,cap)
if __name__ == '__main__':
	main()