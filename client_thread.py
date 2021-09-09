from threading import Thread
import cv2
import client
import socket

PATH = r".\Demos\demo"
HOST = socket.gethostname()
PORT0 = 12340
PORT1 = 12341
PORT2 = 12342
PORT3 = 12343
PORT4 = 12344
PORT5 = 12345

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(PATH+"1.mp4")
cap2 = cv2.VideoCapture(PATH+"2.mp4")
cap3 = cv2.VideoCapture(PATH+"3.mp4")
cap4 = cv2.VideoCapture(PATH+"4.mp4")
cap5 = cv2.VideoCapture(PATH+"5.mp4")

threads = []

client0 = Thread(target = client.tcp_client,args = (PORT0,HOST,cap0,))
threads.append(client0)
client1 = Thread(target = client.tcp_client,args = (PORT1,HOST,cap1,))
threads.append(client1)
client2 = Thread(target = client.tcp_client,args = (PORT2,HOST,cap2,))
threads.append(client2)
client3 = Thread(target = client.tcp_client,args = (PORT3,HOST,cap3,))
threads.append(client3)
client4 = Thread(target = client.tcp_client,args = (PORT4,HOST,cap4,))
threads.append(client4)
client5 = Thread(target = client.tcp_client,args = (PORT5,HOST,cap5,))
threads.append(client5)


for thread in threads:
	thread.start()