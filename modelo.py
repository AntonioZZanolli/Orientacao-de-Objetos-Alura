class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f"Nome: {self._nome} Likes: {self._likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Duração: {self.duracao} minutos - Likes: {self._likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Duração: {self.temporadas} temporadas - Likes: {self._likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._pogramas = programas

    def __getitem__(self, item):
        return self._pogramas[item]

    def __len__(self):
        return len(self._pogramas)


atlanta = Serie("atlanta", 2018, 2)
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Filme("demolidor", 2016, 2)
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()


lista = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist("Fim de semana", lista)

for programa in minha_playlist:
    print(programa)
print(f"Tamanho: {len(minha_playlist.listagem)}")