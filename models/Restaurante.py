from models.Avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"

    def alternar_estado(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    def avaliar(self, cliente, nota):
        if nota <= 5 and nota >= 0:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print("Nota inválida")

    def ver_avaliacoes(self):
        for avaliacao in self._avaliacoes:
            print(avaliacao)

    @property
    def mostrar_media(self):
        if not self._avaliacoes:
            print("Não há avaliações disponíveis.")
            return

        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        media = soma_das_notas / len(self._avaliacoes)
        print(f"A média é: {media:.2f}")
