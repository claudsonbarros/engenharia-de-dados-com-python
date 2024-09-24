# Bootcamp Engenharia de Dados com Python - DIO. NTT DATA 
##Desafio criação de um sistema bancario com Python

###Proposta:
Neste projeto, incrementamos o Sistema Bancário em Python desenvolvido no desafio anterior. Esta nova versão implementa um sistema de banco simples em Python que permite realizar operações básicas como depósito, saque, consulta de extrato, criação de clientes e contas, além de listar contas existentes. Ele utiliza conceitos de Programação Orientada a Objetos (POO) e o módulo `abc` (Abstract Base Classes) para criar transações abstratas.

### Linguagem Utilizada:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Funções

### `exibir_menu()`
Exibe o menu de operações disponíveis para o usuário e retorna a opção escolhida.

**Retorna**:
- A entrada do usuário, indicando a operação desejada.

---

### `formata_cpf(cpf)`
Remove caracteres não numéricos do CPF informado.

**Parâmetros**:
- `cpf`: string contendo o CPF a ser formatado.

**Retorna**:
- String do CPF apenas com números.

---

### `filtrar_cliente(cpf, clientes)`
Verifica se um cliente com o CPF informado existe na lista de clientes.

**Parâmetros**:
- `cpf`: string com o CPF a ser verificado.
- `clientes`: lista de objetos do tipo `Cliente`.

**Retorna**:
- O objeto `Cliente` correspondente, ou `None` se o CPF não for encontrado.

---

### `recuperar_conta_cliente(cliente)`
Recupera a primeira conta de um cliente.

**Parâmetros**:
- `cliente`: objeto do tipo `Cliente`.

**Retorna**:
- A primeira conta do cliente, ou `None` se o cliente não tiver contas.

---

### `depositar(clientes)`
Realiza a operação de depósito na conta de um cliente.

**Parâmetros**:
- `clientes`: lista de clientes.

**Retorna**:
- Nada, apenas exibe mensagens de sucesso ou falha.

---

### `sacar(clientes)`
Realiza a operação de saque na conta de um cliente.

**Parâmetros**:
- `clientes`: lista de clientes.

**Retorna**:
- Nada, apenas exibe mensagens de sucesso ou falha.

---

### `consultar_extrato(clientes)`
Exibe o extrato da conta de um cliente, incluindo transações e saldo atual.

**Parâmetros**:
- `clientes`: lista de clientes.

**Retorna**:
- Nada, apenas exibe o extrato.

---

### `criar_cliente(clientes)`
Cria um novo cliente e o adiciona à lista de clientes.

**Parâmetros**:
- `clientes`: lista de clientes.

**Retorna**:
- A lista atualizada de clientes.

---

### `criar_conta(numero_conta, clientes, contas)`
Cria uma nova conta para um cliente existente e a adiciona à lista de contas.

**Parâmetros**:
- `numero_conta`: número da nova conta a ser criada.
- `clientes`: lista de clientes.
- `contas`: lista de contas.

**Retorna**:
- A lista atualizada de contas.

---

### `listar_contas(contas)`
Exibe todas as contas registradas.

**Parâmetros**:
- `contas`: lista de contas.

**Retorna**:
- Nada, apenas exibe a lista de contas.

---

## Classes

### `transacao` (Abstract Base Class)
Define a estrutura básica de uma transação bancária.

**Propriedades abstratas**:
- `valor`: deve retornar o valor da transação.

**Métodos abstratos**:
- `registrar(self, conta)`: deve implementar a lógica para registrar uma transação em uma conta.

---

### `Cliente`
Representa um cliente do banco.

**Atributos**:
- `endereco`: string contendo o endereço do cliente.
- `contas`: lista de contas associadas ao cliente.

**Métodos**:
- `realizar_transacao(self, conta, transacao)`: executa uma transação em uma conta do cliente.
- `adicionar_contas(self, conta)`: adiciona uma conta à lista de contas do cliente.

---

### `PessoaFisica` (Herda de `Cliente`)
Representa um cliente pessoa física.

**Atributos**:
- `nome`: nome do cliente.
- `data_nascimento`: data de nascimento do cliente.
- `cpf`: CPF do cliente.
- `endereco`: endereço do cliente.

---

### `Conta`
Representa uma conta bancária.

**Atributos**:
- `_saldo`: saldo da conta.
- `_numero`: número da conta.
- `_cliente`: cliente associado à conta.
- `_agencia`: agência bancária da conta.
- `_historico`: histórico de transações da conta.

**Métodos**:
- `nova_conta(cls, cliente, numero)`: cria uma nova conta para um cliente.
- `sacar(self, valor)`: realiza um saque, respeitando o saldo disponível.
- `depositar(self, valor)`: realiza um depósito na conta.

---

### `ContaCorrente` (Herda de `Conta`)
Representa uma conta corrente com limites de saque.

**Atributos**:
- `limite`: limite máximo para um saque.
- `limite_saques`: número máximo de saques permitidos por dia.

**Métodos**:
- `sacar(self, valor)`: realiza o saque, verificando os limites diários e de valor por saque.

---

### `Historico`
Armazena o histórico de transações da conta.

**Atributos**:
- `_transacoes`: lista de transações realizadas na conta.

**Métodos**:
- `adicionar_transacao(self, transacao)`: adiciona uma transação ao histórico.

---

### `Saque` (Herda de `transacao`)
Representa uma transação de saque.

**Atributos**:
- `_valor`: valor do saque.

**Métodos**:
- `registrar(self, conta)`: registra o saque na conta.

---

### `Deposito` (Herda de `transacao`)
Representa uma transação de depósito.

**Atributos**:
- `_valor`: valor do depósito.

**Métodos**:
- `registrar(self, conta)`: registra o depósito na conta.

---

## Execução do Programa
### `main()`
Função principal do programa que exibe o menu e executa as operações conforme a escolha do usuário. Ela faz um loop contínuo até que o usuário escolha a opção de sair (`q`).


