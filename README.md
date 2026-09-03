# Projeto Sockets - Calculadora Cliente-Servidor (TCP)

Trabalho da disciplina T310-16 Projeto de redes convergentes - UNIFOR
Atividade Avaliativa 1 (AV1)

## Equipe

- Tiago Pascoal - Matrícula 2320491
- Victor Menezes - Matrícula 2325183

## Objetivo

Implementação de uma aplicação cliente-servidor usando sockets TCP em Python.
O servidor funciona como uma calculadora: recebe comandos do cliente com uma
operação matemática, processa o cálculo e retorna o resultado pela mesma conexão.

## Como executar

1. Inicie o servidor:

   python3 servidor.py

   O servidor escuta por padrão na porta 9000.
2. Em outro terminal, inicie o cliente:

   python3 cliente.py
3. Digite comandos no formato OPERACAO NUM1 NUM2, por exemplo:

   > SOM 10 20
   > RESULTADO 30
   >
4. Comandos disponíveis: SOM/SOMA, SUB, MUL, DIV, SAIR

## Protocolo

| Comando  | Descrição                   | Exemplo    | Resposta             |
| -------- | ----------------------------- | ---------- | -------------------- |
| SOM/SOMA | Soma dois inteiros            | SOMA 10 20 | RESULTADO 30         |
| SUB      | Subtrai o segundo do primeiro | SUB 50 8   | RESULTADO 42         |
| MUL      | Multiplica dois inteiros      | MUL 6 7    | RESULTADO 42         |
| DIV      | Divisão inteira              | DIV 20 4   | RESULTADO 5          |
| SAIR     | Encerra a conexão            | SAIR       | (conexão encerrada) |

## Tratamento de erros

- Divisão por zero: ERRO: divisao por zero
- Comando desconhecido: ERRO: comando desconhecido
- Formato inválido: ERRO: formato invalido (use: OPERACAO NUM1 NUM2)

## Suporte a múltiplos clientes

O servidor usa uma thread por conexão (threading), permitindo atender
vários clientes simultaneamente sem bloquear.
