import socket
import threading

addres = ('localhost', 12345)

def handle_client(connection,addres):
    print(f'Nova conexao de: {addres}')

    while True:
        data = connection.recv(1024)
        with open("prova_recebido.txt", 'wb') as arquivo:
            arquivo.write(data)
            arquivo.close()

        arquivo1 = open("prova_recebido.txt", "r") 
        arquivo2 = open("gabarito.txt", "r")  

        f1 = arquivo1.readlines()  
        f2 = arquivo2.readlines()  

        correto = 0
        errado = 0

        arquivo1.close()
        arquivo2.close()

        for i in range(0, len(f2)):
            for j in range(0, len(f1)):
                if (f2[i][0] == f1[j][0]):
                    if (f1[j] == f2[i]):
                        correto += 1
                    else:
                        errado += 1

        if(i > j-1):
            errado += i-(j-1)

        
        connection.sendall(str.encode(f'Nome: {f1[0][:-1]} | Acertos: {correto} | Erros: {errado}'))

    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addres)) 
server.listen()
print('Aguardando conexao...')

while True:
    connection, address = server.accept()
    thread = threading.Thread(target=handle_client, args=(connection, address))
    thread.start()
    print(f"CONEXOES ATIVAS: {threading.activeCount() - 1}")