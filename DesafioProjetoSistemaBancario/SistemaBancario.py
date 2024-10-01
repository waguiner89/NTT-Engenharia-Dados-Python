op = 1
saldo = 0
saque = 0
dep = 0
cont_saque = 0
extrato = ""
nome_usuario = input("Digite seu nome: ")

while op > 0:
    op = int(input(f"Olá {nome_usuario}, digite a operação desejada: 1-Depositar / 2-Sacar / 3-Extrato / 0-Encerrar: "))
    if op == 1:
        print()
        dep = float(input(f"{nome_usuario}, digite o valor para depositar: R$ "))
        if dep <= 0:
            print("Não há como depositar valores negativos ou zerados!")
        else:
            saldo += dep
            print(f"Depósito realizado com sucesso {nome_usuario}!")
            extrato += f"Depósito: R$ {dep:.2f}\n"
            print()
    elif op == 2:
        if cont_saque == 3:
            print("Limite máximo de saque atingigo (3). Retorne amanhã para novo saque")
        else:
            print()
            print(f"{nome_usuario}, seu saldo atual é: R$ {saldo}")
            saque = float(input("Digite o valor para sacar: R$ "))
            if saque > 500:
                print("Seu limite diário para saque é R$ 500, escolha outro valor.")
            elif saque > saldo:
                print("Saque solicitado maior que seu saldo na conta.")
                print(f"{nome_usuario}, seu saldo atual é R$ {saldo}.")
            else:
                saldo -= saque
                print(f"Saque realizado com sucesso {nome_usuario}!")
                cont_saque += 1
                extrato += f"Saque: R$ {dep:.2f}\n"
        print()
    elif op == 3:
        print("\nEXTRATO")
        print("Sem registro de movimentações." if not extrato else extrato)
        print(f"\n{nome_usuario}, seu saldo é: R$ {saldo}\n")
    elif op == 0:
        print("Sessão encerrada!")
    else:
        print("Opção errada, escolha entre 1-Depositar / 2-Sacar / 3-Extrato / 0-Encerrar\n")
