
#Define variaveis
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def sacar(valor):
    """
    Método responsavel por realizar a operação de saque respeitando o limite de saques diários 
    e o limite máximo por saque.
    """
    global saldo, extrato,numero_saques

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > limite_saque:
        print("Operação falhou! O valor do saque excede o limite por saque.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques +=1

        print("Operação realizada com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    


def depositar(valor):
    """
    Método responsavel por realizar a operação de deposito respeitando as regras de valores positivos 
    e formatação de mensagem.
    """
    global saldo, extrato

    if valor >0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        print("Operação realizada com sucesso!")
    else:
        print("Operação Falou! O valor informado é inválido")

def consultar_extrato():
    """
    Método responsavel por realizar a operação de consultar extrato.
    """

    global saldo, extrato

    print("\n====================EXTRATO====================")
    print("Não foram realizads movimentações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("===============================================")

def main():

    while True:
        opcao = input(menu)

        if opcao == 'q':
            break
        elif opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)

        elif opcao == 's':
            valor = float(input("Informe o valor do depósito: "))
            sacar(valor)

        elif opcao == 'e':
            consultar_extrato()
        else:
            print("Opção inválida, por favor informe uma das opções informadas")



if __name__ == '__main__':
    main()