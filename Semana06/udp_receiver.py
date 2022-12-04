import socket #importa libs
import select

UDP_IP = "127.0.0.1" #define endereço IP
IN_PORT = 5005 #define porta de entrada
timeout = 3 #define timeout


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# cria objeto sock de classe socket e SOCK_DGRAM define o uso de udp
sock.bind((UDP_IP, IN_PORT))#estabelece conexao com metodo connect do objeto sock da classe socket por UDP

while True:
    data, addr = sock.recvfrom(1024) #recebe o conteudo do socket
    if data: #se conteudo recebido nao for nulo, ele retorna nome arquivo file_name
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb') #abre arquivo

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]: #se pronto
            data, addr = sock.recvfrom(1024) #recebe conteudo do socket
            f.write(data) # e, entao, escreve conteudo no arquivo
        else:
            print("%s Finish!" % file_name)
            f.close()#fecha arquivo
            break
