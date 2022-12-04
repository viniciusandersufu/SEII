import socket #importa bibliotecas
import time
import sys

UDP_IP = "127.0.0.1" #define endereço IP
UDP_PORT = 5005 #define porta
buf = 1024 #define tamanho buffer
file_name = sys.argv[1] #recebe nome do arquivo como argumento de linha do terminal


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria objeto sock de classe socket e SOCK_DGRAM define o uso de udp
sock.sendto(file_name, (UDP_IP, UDP_PORT))#estabelece conexao com metodo connect do objeto sock da classe socket por UDP
print ("Sending %s ..." % file_name)

f = open(file_name, "r") #abre arquivo
data = f.read(buf) #retorna conteudo do arquivo
while(data):#enquanto a msg for nao nula o while manda msg por UDP
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() #fecha conexao socket
f.close() #fecha arquivo
