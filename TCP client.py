import socket

target_host = "address of the target host"
target_port = 80

# создаём объект сокета, параметр AF_INET указывает на то, что мы будем использовать адрес IPv4 или сетевое время, а SOCK_STREAM означает, что клиент будет работать по TCP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключаем клиент.
client.connect((target_host, target_port))

# отправляем какие-нибудь данные.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# принимаем какие-нибудь данные.
response = client.recv(4096)

print(response.decode())
client.close()