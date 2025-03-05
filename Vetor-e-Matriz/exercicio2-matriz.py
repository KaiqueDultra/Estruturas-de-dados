import numpy as np

class Matriz:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ultima_posicao = 0
        self.valores = np.zeros((4, 4), dtype=str)
    
    def insere(self, valor):
        # Verificando se ainda temos espaço na matriz
        if self.ultima_posicao < self.tamanho:
            linha = self.ultima_posicao // 4 # Calculando a linha com base no índice
            coluna = self.ultima_posicao % 4 # Calculando a coluna com base no índice
            self.valores[linha, coluna] = valor
            self.ultima_posicao += 1 # Avançando para a proxima posição
        
    def imprime(self):
        if self.ultima_posicao == 0:
            print('A matriz está vazia.')
        else:
            print(self.valores)

matriz = Matriz(16)
matriz.insere('a')
matriz.insere('b')
matriz.insere('c')
matriz.insere('d')
matriz.insere('e')
matriz.insere('f')
matriz.insere('g')
matriz.insere('h')
matriz.insere('i')
matriz.insere('j')
matriz.insere('k')
matriz.insere('l')
matriz.insere('m')
matriz.insere('n')
matriz.insere('o')
matriz.insere('p')
matriz.imprime()
            