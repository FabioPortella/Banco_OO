class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(150)

print(f"Saldo de R${conta.mostrar_saldo()},00")
print(f"Agencia {conta.nro_agencia}")