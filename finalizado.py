def exibir_menu():
    menu = """
========= BANCO PYTHON =========

 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Novo Cliente
 [5] Nova Conta
 [6] Listar Contas
 [0] Sair

================================
=> """
    return input(menu)


def realizar_deposito(saldo, valor, extrato):
    if valor <= 0:
        print("Valor inválido. O depósito deve ser maior que zero.")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")
    return saldo, extrato


def realizar_saque(saldo, valor, extrato, limite, saques_realizados, max_saques):
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite de saque.")
    elif saques_realizados >= max_saques:
        print("Número máximo de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, saques_realizados


def mostrar_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")


def buscar_cliente(cpf, clientes):
    return next((cliente for cliente in clientes if cliente["cpf"] == cpf), None)


def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if buscar_cliente(cpf, clientes):
        print("Já existe um cliente cadastrado com este CPF.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (Rua, Bairro, Cidade - UF): ")

    clientes.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Cliente cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do titular: ")
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "titular": cliente}
    else:
        print("CPF não encontrado. Cadastre o cliente antes de criar uma conta.")
        return None


def exibir_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n======= LISTA DE CONTAS =======")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['titular']['nome']}")
        print("===============================")
    print()


def main():
    LIMITE_SAQUES = 3
    AGENCIA_PADRAO = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    clientes = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, saques_realizados = realizar_saque(
                saldo, valor, extrato, limite, saques_realizados, LIMITE_SAQUES
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato)

        elif opcao == "4":
            cadastrar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA_PADRAO, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            exibir_contas(contas)

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
