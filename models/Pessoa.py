class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def set_profissao(self, new_profissao):
        self._profissao = new_profissao

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} Profissao: {self.profissao}"

    def aniversario(self):
        self._idade += 1

    def saldacao(self):
        print(f"Saldações {self.profissao}")
