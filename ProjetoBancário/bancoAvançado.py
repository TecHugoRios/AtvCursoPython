
def menu(saldo):
    print(f"""
================ MENU ===================

Bem vindo! Seu saldo é R$ {saldo}

1 - Depositar.

2 - Sacar.

3 - Extrato.

4 - Novo Usuário.

5 - Criar Conta.

0 - Sair.
========================================= """)

def depositar(valor,saldo,extrato):
    if valor < 0 :
        print("Insira um valor positivo")
    else:
        saldo += valor
        extrato += f"Depósito:\t ++ R$ {valor:.2f}\n"
        print(f"O valor depositado foi R${valor} e o seu saldo agora é de R${saldo}")
    
    return saldo, extrato

def sacar(valor,saldo,extrato,LIMITE_SAQUE,limite_diario):
     saques_realizados = 0
     if saques_realizados == LIMITE_SAQUE:
        print("Limite de saque diário atingido, tente novamente no dia seguinte.")
     if valor < 0 :
        print("Insira um valor positivo!")
     elif valor > 500 :
        print(f"Você só pode sacar o máximo de R${limite_diario} diários")
     elif valor > saldo :
        print("Saldo Insuficiente!")
     else:
        saldo -= valor 
        extrato += f"Saque:\t\t -- R$ {valor:.2f}\n"
        print(f"O valor sacado foi R${valor} e o seu saldo agora é de R${saldo}")
        saques_realizados += 1

     return saldo,extrato
        
def exibir_extrato(saldo,extrato):
    print("================ EXTRATO ================")
    print(f"{extrato}\n")
    print(f"Saldo: \t\tR${saldo:.2f}\t\n")
    print("=========================================")

def criar_usuario(usuario):

    print("""
================ Sign In ================
        
    Bem vindo ao nosso Banco
    crie uma conta.

=========================================
             
""")
    
    cpf = input("Escreva seu CPF: ")

    if [usuario for elemento in usuario if elemento["cpf"] == cpf]:
        print("Esse CPF já está registrado")
        return

    nome_usuario = input("Escreva seu nome completo: ")
    data_nascimento = input("Escreva sua data de nascimento (dd-mm-aaaa): ")
    usuario.append({"nome": nome_usuario, "data_nascimento": data_nascimento, "cpf": cpf})

def criar_conta(agencia,numero_conta,usuario):
    cpf = input("Informe o CPF para criar a conta: ")

    if [usuario for elemento in usuario if elemento["cpf"] == cpf]:
        print("\nConta criada com sucesso!\n")

        print(f"Agência: \t\t{agencia}")
        print(f"Nº da Conta: \t\t{numero_conta}")

        for i in usuario:
            chave = "nome"
            for dict in usuario:
              valor = dict.get(chave)      
        
        print(f"Titular: \t\t{valor}")

        return {"agencia":agencia,"numero_conta": numero_conta, "usuario":usuario}
    
    print("ERRO: CPF não encontrado")

def programa():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    limite_diario = 500
    numero_conta = ""
    usuarios = []
    contas = []

    execute = False

    while True:
        #if execute != True:
        #    criar_usuario()
        #    execute = True
      
        menu(saldo=saldo)
        opcao = int(input())

        if opcao == 1: #depositar
            valor = float(input("\nInsira o valor que deseja depositar: "))
            saldo,extrato = depositar(valor,saldo,extrato)
        elif opcao == 2:#sacar
            valor = float(input("Insira o valor que deseja sacar: "))
            saldo,extrato = sacar(valor=valor,saldo=saldo,extrato=extrato,LIMITE_SAQUE=LIMITE_SAQUE,limite_diario=limite_diario)
        elif opcao == 3:#extrato
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta =  criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 0:
            print("Obrigado por utilizar o nosso programa de banco")
            break
            

programa()