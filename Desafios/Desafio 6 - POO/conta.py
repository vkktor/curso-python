from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=500):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()
