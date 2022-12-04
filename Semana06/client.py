import socket

#Define header, porta para comunicação, formato de decode, endereco IP e concatena formato para o bind
HEADER = 64 
PORT = 5050 
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "!DISCONNECT" 
SERVER = "127.0.1.1" 
ADDR = (SERVER, PORT)

#Objeto de comunicação via socket que define, com AF_INET, um padrao de comunicacao Ethernet.
#SOCK_STREAM define uso de TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDR)#Define endereço ao objeto socket criado

#função para envio de msg
def send(msg):
	message = msg.encode(FORMAT) #faz o encode da msg com o formato previamente definido
	msg_length = len(message) #retorna tamanho da msg
	send_length = str(msg_length).encode(FORMAT) 
	send_length += b' ' * (HEADER - len(send_length)) 
	client.send(send_length) #envia tamanho da msg
	client.send(message) #envia msg
	print(client.recv(2048).decode(FORMAT))

#envia diversas msgs e dps envia msg para desconectar
send("Hello world!") 
input() 
send("Hello Everyone!") 
input() 
send("Hello Lucas!")

send(DISCONNECT_MESSAGE)
