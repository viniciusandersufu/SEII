import socket#importa biblioteca socket

TCP_IP = "127.0.0.1"#define endereço IP
FILE_PORT = 5005 #define porta para envio do nome do arquivo
DATA_PORT = 5006 #define porta para envio do conteudo do arquivo
timeout = 3 #define timeout
buf = 1024 #define tamanho buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria objeto de comunicação socket e define o uso de TCP por meio de SOCK_STREAM
sock_f.bind((TCP_IP, FILE_PORT))#estabelece conexao com metodo connect do objeto sock_f da classe socket por TCP
sock_f.listen(1)#Estabelece conexao com socket e espera por uma mensagem


sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria objeto de comunicação socket e define o uso de TCP por meio de SOCK_STREAM
sock_d.bind((TCP_IP, DATA_PORT))#estabelece conexao com metodo connect do objeto sock_d da classe socket por TCP
sock_d.listen(1)#Estabelece conexao com socket e espera por uma mensagem


while True:
    conn, addr = sock_f.accept() #espera requisicao de conexao e a aceita
    data = conn.recv(buf) #se conteudo nao for nulo ele eh printado no terminal
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb') #abre o arq com o nome definido

    conn, addr = sock_d.accept()#espera requisicao de conexao e a aceita
    while True:
        data = conn.recv(buf) #recebe arquivo e escreve seu conteudo no terminal s enao nulo
        if not data:
            break
        f.write(data)

    print ("%s Finish!" % file_name) #print que finalizou o recebimento do arquivo de nome file_name
    f.close()#fecha arquivo
