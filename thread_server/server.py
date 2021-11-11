#Нужные модули
import socket
import threading


def proc():
	socketserv = socket.socket()      #Создаем сокет
	socketserv.bind(('', 9090))       #Привязываем к айпи и порту  
	socketserv.listen(0)              #Запускаем режим прослушивания
	connection, address = socketserv.accept()           #Принимаем подключения
	print(address)

	message = '1234'        #Сообщения

	while True:        #Цикл для постоянного подключения
		data = connection.recv(1024)
		if not data:
			break
		message += data.decode()
		connection.send(data)


	connection.close()   #закрываем соединения

p1 = threading.Thread(target=proc(), name="t1", args=["1"])
p2 = threading.Thread(target=proc(), name="t2", args=["2"])
p1.start()
p2.start()