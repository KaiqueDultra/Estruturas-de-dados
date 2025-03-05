import numpy as np

class Vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    # Método para inserir valores no vetor. 
    def insere(self, valor):
        # Verifica se a capacidade máxima do vetor foi atingida
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima do vetor atingida.')
            return 
            
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor # Insere o valor na ultima posicao do vetor.
    
    # Metodo para imprimir os valores do vetor.    
    def imprime(self):
        # Verifica se o vetor está vazio.
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

vetor = Vetor(10)
vetor.insere(10)
vetor.insere(20)
vetor.insere(30)
vetor.insere(40)
vetor.insere(50)
vetor.insere(60)
vetor.insere(70)
vetor.insere(80)
vetor.insere(90)
vetor.insere(100)
vetor.imprime()