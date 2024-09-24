
import re

#Define variaveis
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []
numero_conta = 1

def exibir_menu():
    menu = """
    =================  Menu  =================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair 
    =>"""
    return input(menu)

def sacar(*, saldo,valor,extrato,limite,numero_saques,limite_saques):
    """
    Método responsavel por realizar a operação de saque respeitando o limite de saques diários 
    e o limite máximo por saque.
    """
    if valor > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > limite_saque:
        print("\nOperação falhou! O valor do saque excede o limite por saque.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques +=1
        print("\nSaque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return (saldo,extrato,numero_saques)

def depositar(valor,saldo,extrato, /):
    """
    Método responsavel por realizar a operação de deposito respeitando as regras de valores positivos 
    e formatação de mensagem.
    """
    if valor >0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"

        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação Falou! O valor informado é inválido")
    return (saldo,extrato)

def consultar_extrato(saldo, /, *,extrato):
    """
    Método responsavel por realizar a operação de consultar extrato.
    """
    print("\n====================EXTRATO====================")
    print("Não foram realizads movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("===============================================")

def formata_cpf(cpf):
    """
    Método responsavel por revomer caracteres do cpf, retornando apenas números
    """
    cpf_formatado = re.sub(r'\D', '', cpf)
    return cpf_formatado

def filtrar_usuario(cpf,usuarios):
    """
    Método responsavel por verificar se o cpf existe na lista de usuários
    """
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        else:
            None

def criar_usuario(usuarios):
    """
    Método responsavel por criar um novo usuário
    """

    cpf = input('Informar o CPF (Somente números): ')
    cpf = formata_cpf(cpf)
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\nJá existe um usuário com este CPF")
        return
    
    print("=======================Cadastro de usuário=======================")
    nome_usuario = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data nascimento (DD-MM-YYYY): ")
    print("----------------------------Endereço----------------------------")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")

    endereco= f'{logradouro}, {numero} - {bairro} - {cidade}/{uf}'

    usuario = {"nome":nome_usuario,
               "data_nascimento":data_nascimento,
               "cpf":cpf,
               "endereco":endereco}
    usuarios.append(usuario)
    
    print('\nUsuário criado com sucesso!')
    return usuarios

def criar_conta(agencia,numero_conta,usuarios,contas):
    """
    Método responsavel por criar uma nova conta
    """

    cpf = input('Informar o CPF do usuário: ')
    cpf = formata_cpf(cpf)
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        conta = {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
        contas.append(conta)
        print('\nConta criada com sucesso!')
    else:
        print("\nUsuário não encontrado, fluxo de criação encerrado")
    
    return contas

def listar_contas(contas):
    """
    Método responsavel por listar todas as contas
    """

    for conta in contas:
        print(f"\nAgencia: {conta["agencia"]}"
              + f"\nNúmero conta: {conta["numero_conta"]}"
              + f"\nTitular: {conta["usuario"]["nome"]}")

def main():
    global saldo, extrato,numero_saques,LIMITE_SAQUES,limite_saque,usuarios,AGENCIA,contas,numero_conta
  

    while True:
        opcao = exibir_menu()

        if opcao == 'q':
            break
        elif opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            (saldo,extrato) = depositar(valor,saldo,extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            (saldo,extrato,numero_saques) = sacar(saldo=saldo
                                                  ,valor=valor
                                                  ,extrato=extrato
                                                  ,limite=limite_saque
                                                  ,numero_saques=numero_saques
                                                  ,limite_saques=LIMITE_SAQUES)

        elif opcao == 'e':
            consultar_extrato(saldo,extrato=extrato)
        elif opcao == 'nu':
            usuarios = criar_usuario(usuarios)

        elif opcao == 'nc':
            contas = criar_conta(AGENCIA,numero_conta,usuarios,contas)
            numero_conta += 1
        elif opcao == 'lc':
            listar_contas(contas)
        else:
            print("\nOpção inválida, por favor informe uma das opções informadas")



if __name__ == '__main__':
    main()