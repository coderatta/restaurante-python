class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Titular: {self.titular}\nSaldo: {self.saldo}"

    def ativar_conta(self):
        self._ativo = True

    @classmethod
    def codigo_banco(cls):
        return "223"
