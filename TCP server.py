import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT)) # передаём IP-адрес и номер порта для прослушивания.
	server.listen(5) # запускаем прослушивание порта с количеством отложенных соединений <= 5.
	print(f'[*] Listening on {IP}:{PORT}')

	while True:
		client, address = server.accept() # принимаем входящие соединения, сохраняем значение клиентского сокета в client, а подробности об удалённом соединении в address.
		print(f'[*] Accepted connection from {address[0]}:{address[1]}')
		client_handler = threading.Thread(target=handle_client, args=(client,)) # создаём объект потока через вызов функции handle_client, в качестве аргумента передаем значение сокета клиента.
		client_handler.start()

def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f'[*] Received: {request.decode("utf-8")}')
		sock.send(b'ACK')

if __name__ == '__main__':
	main()