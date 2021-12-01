import socket

target_host = "address of the target host"
target_port = 9997

# создаем объект сокета, аргумент SOCK_DGRAM указывает на тип протокола - UDP.
client = socket.socket(socket.AF_NET, socket.SOCK_DGRAM)

# отправляем какие-нибудь данные.
client.sendto(b"AAABBBCCC", (target_host, target_port))

# принимаем какие-нибудь данные.
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()