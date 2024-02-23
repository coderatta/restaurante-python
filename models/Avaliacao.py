class Avaliacao:
    def __init__(self, cliente, nota):
        self._nota = nota
        self._cliente = cliente

    def __str__(self) -> str:
        return f"Nome: {self._cliente}, Nota: {self._nota}"

    @property
    def nota(self):
        return self._nota
