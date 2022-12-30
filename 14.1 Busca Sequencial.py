class musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class buscador:
    def busca_por_titulo(self, seq, x):
        for i in range(len(seq)):
            if seq[i].titulo == x:
                return i
        return - 1

    def vamos_buscar(self):
        playlist = [musica("Facas","Bruno e Marrone","Marrone","2021"),musica("E ai ja era","Jorge e Matheus","Matheus","2013"),musica("Brasilia amarela","Mamonas Assassinas","leo","1994")]

        onde_achou = self.busca_por_titulo(playlist,"E ai ja era")

        if onde_achou == -1:
            print("Nao esta na playlist")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = ', ')

buscador().vamos_buscar()