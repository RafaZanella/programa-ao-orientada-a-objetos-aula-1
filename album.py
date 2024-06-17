class Album:
    def __init__(self, titulo, ano, faixas):
       self.titulo = titulo
       self.ano = ano
       self.faixas = faixas

    def mostrar_info(selff):
        print(f'Album: {self.titulo}, Ano:{self.ano} ')
        print(' Faixas:')
        for faixa in self.faixas:
            print(f' {faixa}')

    


