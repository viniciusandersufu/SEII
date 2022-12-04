import socket #importa biblioteca socket
import sys #importa lib sys

TCP_IP = "127.0.0.1" #define endereço IP
FILE_PORT = 5005 #define porta para envio do nome do arquivo
DATA_PORT = 5006 #define porta para envio do conteudo do arquivo
buf = 1024 #define tamanho buffer
file_name = sys.argv[1] #recebe nome do arquivo como argumento de linha do terminal

#trata exceçoes em try
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria objeto de comunicação socket e define o uso de TCP por meio de SOCK_STREAM
    sock.connect((TCP_IP, FILE_PORT))#estabelece conexao com metodo connect do objeto sock da classe scoket por TCP
    sock.send(file_name) #envia o arquivo com metodo send
    sock.close() #finaliza a comunicaçao fechando socket

    print("Sending %s ..." % file_name) #printa no terminal sobre o envio do file_name

    f = open(file_name, "rb") #abre arquivo com nome file_name
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria objeto de comunicação socket e define o uso de TCP pr meio de SOCK_STREAM
    sock.connect((TCP_IP, DATA_PORT))#cria objeto de comunicação socket e define o uso de TCP pr meio de SOCK_STREAM
    data = f.read() #retorna com metodo read() o conteudo do arquivo
    sock.send(data) #envia os dados do arquivo

finally:
    sock.close()#finaliza ultima conexão aberta
    f.close()#fecha o arquivo aberto
