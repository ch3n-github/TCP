from threading import Thread
import server


PORT0 = 12340
PORT1 = 12341
PORT2 = 12342
PORT3 = 12343
PORT4 = 12344
PORT5 = 12345


threads = []

server0 = Thread(target = server.tcp_server,args = (PORT0,))
threads.append(server0)
server1 = Thread(target = server.tcp_server,args = (PORT1,))
threads.append(server1)
server2 = Thread(target = server.tcp_server,args = (PORT2,))
threads.append(server2)
server3 = Thread(target = server.tcp_server,args = (PORT3,))
threads.append(server3)
server4 = Thread(target = server.tcp_server,args = (PORT4,))
threads.append(server4)
server5 = Thread(target = server.tcp_server,args = (PORT5,))
threads.append(server5)

for thread in threads:
	thread.start()
