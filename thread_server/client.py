    #Нужные модули
import socket         

socketserv = socket.socket()       #Создаем сокет
socketserv.setblocking(1)
socketserv.connect(('localhost', 9090))        #Привязываем к айпи и порту 

message = "Hi!"
socketserv.send(message.encode())         #Сообщения

data = socketserv.recv(1024)

socketserv.close()         #закрываем соединения

print(data.decode()) #Выводим data