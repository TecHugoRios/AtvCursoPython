saldo = 0
extrato = ""
limite_diario = 500
LIMITE_SAQUE = 3
saques_realizados = 0

menu= f"""
================ MENU ================

1 - Depositar.

2 - Sacar.

3 - Extrato.

0 - Sair.
====================================== """

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Insira o valor que deseja depositar: "))
        if valor < 0 :
            print("Insira um valor positivo")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"O valor depositado foi {valor} e o seu saldo agora é de {saldo}")
    elif opcao == 2:
        if saques_realizados == LIMITE_SAQUE:
            print("Limite de saque diário atingido, tente novamente no dia seguinte.")
            break
        valor = float(input("Insira o valor que deseja sacar: "))
        if valor < 0 :
            print("Insira um valor positivo!")
        elif valor > 500 :
            print(f"Você só pode sacar o máximo de R${limite_diario} diários")
        elif valor > saldo :
            print("Saldo Insuficiente!")
        else:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"O valor sacado foi {valor} e o seu saldo agora é de {saldo}")

        saques_realizados += 1

    elif opcao == 3:
        print("================ EXTRATO ================")
        print(f"{extrato}")
        print("=========================================")
        
    elif opcao == 0:
        print("Obrigado por utilizar o nosso programa de banco")
        break
        

