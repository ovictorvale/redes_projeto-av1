import socket 

HOST = "127.0.0.1"
PORT = 9000

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.connect((HOST, PORT))

    print(f"Conectado ao servidor: {HOST} : {PORT}")
    print("Escolha uma das operações indicadas:\n SOM: Soma;\n SUB: Subtração;\n MUL: Multiplicação;\n DIV: Divisão;\n SAIR.")

    while True:
        comando = input("> ").strip()

        if not comando:
            continue

        cliente.sendall(comando.encode("utf-8"))

        if comando.upper() == "SAIR":
            resposta = cliente.recv(1024).decode("utf-8")
            print(resposta)
            break

        resposta = cliente.recv(1024).decode("utf-8")

        print(resposta)

    cliente.close()

    print("Conexão encerrada.")

if __name__ == "__main__":
    iniciar_cliente()
