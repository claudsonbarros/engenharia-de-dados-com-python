from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import re

def exibir_menu():
    """
        Exibe o menu de operações disponíveis para o usuário e retorna a opção escolhida.
        
    """

    menu = """
    =================  Menu  =================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Cliente
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair 
    =>"""
    return input(menu)

class transacao(ABC):
    """
    Define a estrutura básica de uma transação bancária.

    Propriedades abstratas:
        valor: deve retornar o valor da transação.
    
    Métodos abstratos:
        registrar(self, conta): deve implementar a lógica para registrar uma transação em uma conta.
    """
    @property
    @abstractproperty
    def valor(delf):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Cliente:
    """
    Representa um cliente do banco.

    Atributos:
        endereco: string contendo o endereço do cliente.
        contas: lista de contas associadas ao cliente.

    Métodos:
        realizar_transacao(self, conta, transacao): executa uma transação em uma conta do cliente.
        adicionar_contas(self, conta): adiciona uma conta à lista de contas do cliente.
    """
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta,transacao):
        transacao.registrar(conta)

    def adicionar_contas(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    """
    Representa um cliente pessoa física.

    Atributos:
        nome: nome do cliente.
        data_nascimento: data de nascimento do cliente.
        cpf: CPF do cliente.
        endereco: endereço do cliente.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf 


class Conta:
    """
    Representa uma conta bancária.

    Atributos:
        _saldo: saldo da conta.
        _numero: número da conta.
        _cliente: cliente associado à conta.
        _agencia: agência bancária da conta.
        _historico: histórico de transações da conta.

    Métodos:
        nova_conta(cls, cliente, numero): cria uma nova conta para um cliente.
        sacar(self, valor): realiza um saque, respeitando o saldo disponível.
        depositar(self, valor): realiza um depósito na conta.
    """
    def __init__(self, numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._cliente = cliente 
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self , valor):
        """
        Método responsavel por realizar a operação de saque respeitando o limite de saques diários 
        e o limite máximo por saque.
        """
        saldo = self.saldo

        if valor > saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return False
    
    def depositar(self, valor):
        """
            Método responsavel por realizar a operação de deposito respeitando as regras de valores positivos 
            e formatação de mensagem.
        """
        if valor >0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
        return True

class ContaCorrente(Conta):
    """
    Representa uma conta corrente com limites de saque.

    Atributos:
        limite: limite máximo para um saque.
        limite_saques: número máximo de saques permitidos por dia.
        
    Métodos:
        sacar(self, valor): realiza o saque, verificando os limites diários e de valor por saque.
    """
    def __init__(self,numero,cliente,limite = 500,limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        
        numero_saques = len([trans for trans in self.historico.transacoes if trans["tipo"] == Saque.__name__])

        if numero_saques >= self.limite_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        elif valor > self.limite:
            print("\nOperação falhou! O valor do saque excede o limite por saque.")
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
                Agência:\t{self.agencia}
                CC:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
                """
    
class Historico():
    """
    Armazena o histórico de transações da conta.

    Atributos:
        _transacoes: lista de transações realizadas na conta.

    Métodos:
        adicionar_transacao(self, transacao): adiciona uma transação ao histórico.
    """
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

class Saque(transacao):
    """
    Representa uma transação de saque.

    Atributos:
        _valor: valor do saque.

    Métodos:
        registrar(self, conta): registra o saque na conta.
    """
    def __init__(self,valor):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(transacao):
    """
    Representa uma transação de depósito.

    Atributos:
        _valor: valor do depósito.
    Métodos:
        registrar(self, conta): registra o depósito na conta.
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        if conta.depositar(self.valor):
           conta.historico.adicionar_transacao(self) 

def formata_cpf(cpf):
    """
    Remove caracteres não numéricos do CPF informado.
    
    Parâmetros:
        cpf: string contendo o CPF a ser formatado.
    """
    cpf_formatado = re.sub(r'\D', '', cpf)
    return cpf_formatado

def filtrar_cliente(cpf,clientes):
    """
    Verifica se um cliente com o CPF informado existe na lista de clientes.
    
    Parâmetros:
        cpf: string com o CPF a ser verificado.
        clientes: lista de objetos do tipo Cliente.
    """
    for cli in clientes:
        if cli.cpf == cpf:
            return cli
        else:
            None

def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta de um cliente.

    Parâmetros:
        cliente: objeto do tipo Cliente.
    """
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    """
    Realiza a operação de depósito na conta de um cliente.

    Parâmetros:
        clientes: lista de clientes.
    """
    cpf = formata_cpf(input("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\nCliente não encontrado."
              )
        return
    
    valor = float(input("Informe o valor do depósito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)
    
def sacar(clientes):
    """
    Realiza a operação de saque na conta de um cliente.

    Parâmetros:
        clientes: lista de clientes.
    """
    cpf = formata_cpf(input("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\nCliente não encontrado."
              )
        return
    
    valor = float(input("Informe o valor do saque:"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def consultar_extrato(clientes):
    """
    Exibe o extrato da conta de um cliente, incluindo transações e saldo atual.

    Parâmetros:
        clientes: lista de clientes.
    """
    cpf = formata_cpf(input("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\nCliente não encontrado."
              )
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n====================EXTRATO====================")

    h_transacoes = conta.historico.transacoes

    extrato = ""
    if not h_transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in h_transacoes:
            extrato += f"\n{transacao["tipo"]}:\n\t\tR$ {transacao["valor"]:.2f}"
    print(extrato)
    print(f"\nSaldo: \t\tR$ {conta.saldo:.2f}")
    print("===============================================")

def criar_cliente(clientes):
    """
    Cria um novo cliente e o adiciona à lista de clientes.

    Parâmetros:
        clientes: lista de clientes.
    """

    cpf = formata_cpf(input('Informe o CPF (somente números): '))
    cliente = filtrar_cliente(cpf,clientes)
    
    if cliente:
        print("\nJá existe um cliente com este CPF")
        return
    
    print("=======================Cadastro de cliente=======================")
    nome_usuario = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data nascimento (DD-MM-YYYY): ")
    print("----------------------------Endereço----------------------------")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")

    endereco= f'{logradouro}, {numero} - {bairro} - {cidade}/{uf}'

    cliente = PessoaFisica(nome=nome_usuario,data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    
    print('\nCliente criado com sucesso!')
    return clientes

def criar_conta(numero_conta,clientes,contas):
    """
    Cria uma nova conta para um cliente existente e a adiciona à lista de contas.

    Parâmetros:
        numero_conta: número da nova conta a ser criada.
        clientes: lista de clientes.
        contas: lista de contas.
    """

    cpf = formata_cpf(input('Informe o CPF (somente números): '))
    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        print('\nConta criada com sucesso!')
    else:
        print("\nCliente não encontrado, fluxo de criação encerrado!")
    
    return contas

def listar_contas(contas):
    """
    Exibe todas as contas registradas.

    Parâmetros:
        contas: lista de contas.
    """

    for conta in contas:
        print("="*100)
        print(str(conta))

def main():
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        opcao = exibir_menu()

        if opcao == 'q':
            break
        elif opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            consultar_extrato(clientes)
        elif opcao == 'nu':
            clientes = criar_cliente(clientes)
        elif opcao == 'nc':
            contas = criar_conta(numero_conta,clientes,contas)
            numero_conta += 1
        elif opcao == 'lc':
            listar_contas(contas)
        else:
            print("\nOpção inválida, por favor informe uma das opções informadas")



if __name__ == '__main__':
    main()