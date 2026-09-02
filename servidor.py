import socket
import threading

HOST = "0.0.0.0"
PORT = 9000

def processar_comando(mensagem):
    partes = mensagem.split()

    if not partes:
        return "ERRO: formato invalido (use: OPERACAO NUM1 NUM2)"

    operacao = partes[0].upper()

    if operacao == "SAIR":
        if len(partes) == 1:
            return None

        return "ERRO: formato invalido (use: OPERACAO NUM1 NUM2)"

    operacoes_validas = {"SOM", "SUB", "MUL", "DIV"}

    if operacao not in operacoes_validas:
        return "ERRO: comando desconhecido"

    if len(partes) != 3:
        return "ERRO: formato invalido (use: OPERACAO NUM1 NUM2)"

    try:
        numero1 = int(partes[1])
        numero2 = int(partes[2])

    except ValueError:
        return "ERRO: formato invalido (use: OPERACAO NUM1 NUM2)"

    if operacao == "SOM":
        resultado = numero1 + numero2

    elif operacao == "SUB":
        resultado = numero1 - numero2

    elif operacao == "MUL":
        resultado = numero1 * numero2

    elif operacao == "DIV":
        if numero2 == 0:
            return "ERRO: divisao por zero"

        resultado = numero1 // numero2

    return f"RESULTADO {resultado}"


def atender_cliente(conexao, endereco):
    print(f"[CONECTOU] {endereco[0]} : {endereco[1]}")

    try: 
        while True:
            dados = conexao.recv(1024)

            if not dados:
                break

            mensagem = dados.decode("utf-8").strip() 

            print(f"[RECEBIDO] {endereco} : {mensagem}")

            resposta = processar_comando(mensagem)

            if resposta is None:
                break

            conexao.sendall(resposta.encode("utf-8"))

    finally:
        conexao.close()
        print(f"DESCONECTOU {endereco[0]} : {endereco[1]}")



def iniciar_servidor():
    #AF_INET:  informa que será usado ipv4
    #Sock_tream: informa que será usado o protocolo tcp
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind((HOST, PORT)) # A estrutura bind faz a associação entre o socket, o endereço ip e a porta.
    #obs: IP indetifica o host e porta identifica o proceso/ serviço

    servidor.listen() #indica que o socket está agurdando uma requisição do cliente.

    print(f"[SERVIDOR] Aguarde conexões na porta {PORT}")

    while True: #mantem a conexão aberta.
        conexao, endereco = servidor.accept() #O acecpt retona duas informações, conexão (socket adotado) e endereco (ipcliente e portacliente)

        thread = threading.Thread( #possiblita receber múltiplos comandos do mesmo cliente.
            target=atender_cliente,
            args=(conexao, endereco)
        )

        thread.start()

if __name__ == "__main__":
    iniciar_servidor()