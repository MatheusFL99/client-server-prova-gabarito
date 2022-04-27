import socket

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    arquivo = open("prova.txt", "rb")
    # começa a ler o arquivo e armazenar em um buffer
    data = arquivo.read(1024)

    while (data):
        client.send(data)  # envia o condeudo do buffer para o servidor
        data = arquivo.read(1024)
    print('Arquivo enviado!')

    resposta = client.recv(1024)
    print(resposta)


    fechar_conexao = input('Fechar conexao com o cliente? Y/n ').lower()
    if (fechar_conexao == 'y'):
        client.close()
        break