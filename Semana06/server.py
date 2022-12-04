import socket 
import threading

#Define header, porta para comunicação, formato de decode, endereco IP e concatena formato para o bind
HEADER = 64 
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT) 
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "!DISCONNECT"

#Objeto de comunicação via socket que define, com AF_INET, um padrao de comunicacao Ethernet.
#SOCK_STREAM define uso de TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)#Define endereço ao objeto socket criado

#funçao que realiza handling(lida) com as novas requisições na rede
def handle_client(conn, addr):
	print (f"[NEW CONNECTION] {addr} connected.")
	
	connected = True 
	while connected: #laço espera por nova msg
		msg_length = conn.recv(HEADER).decode(FORMAT) #retorna o tamanho da msg 
		if msg_length:
			msg_length = int(msg_length) 
			msg = conn.recv(msg_length).decode(FORMAT) 
			if msg == DISCONNECT_MESSAGE: # se a msg do cliente for igual DISCONNECT_MESSAGE, connected se torna false e o cliente é desconectado
				connected = False

			print(f"[{addr}] {msg}") 
			conn.send("Msg received".encode(FORMAT))
	conn.close()

#funcao que inicia socket
def start():
	server.listen() #estabelece conexao com socket e espera por msg
	print(f"[LISTENING] Server is listening on {SERVER}") 
	while True:#laço que espera conexão de um cliente
		conn, addr = server.accept() #espera conexao de cliente e a aceita
		thread = threading.Thread(target=handle_client, args=(conn, addr)) #cria thread de conexao com a funçao handle_client, usando a ultima conexao aceita
		thread.start() #starta a thread criada 
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...") 
start()#inicia o socket server
