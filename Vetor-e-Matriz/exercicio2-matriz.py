import numpy as np

class Matriz:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ultima_posicao = -1
        self.valores = np.zeros((4, 4), dtype=str)
    
    def insere(self, valor):
        if self.ultima_posicao == self.tamanho -1:
            print('Capacidade máxima da matriz atingida.')
            return
        
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print('A matriz está vazia.')
        else:
            print(self.valores)

matriz = Matriz(16)
matriz.insere('a')
matriz.insere('b')
matriz.imprime()
            