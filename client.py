#!/usr/bin/python
#-*-coding:utf-8 -*-

import socket
import cv2
import numpy
import struct
def video_write(port,cap):
	
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# 连接服务端

	host = socket.gethostname()
	address_server = (host, 12340)
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

	video_write(12340,cap)
if __name__ == '__main__':
	main()