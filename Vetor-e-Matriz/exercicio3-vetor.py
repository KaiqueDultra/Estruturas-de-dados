def main():
    vetor = [10, 30, 41, 55, 66, 78, 89, 90, 1, 2]
    
    valor = int(input('Digite um valor a ser procurado no vetor: '))
    
    encontrado = False
    
    # i é o índice do vetor e v é o valor que está nesse índice.
    for i, v in enumerate(vetor):
        if v == valor:
            print(f"O valor digitado {valor} se encontra na posição {i} do vetor.")
            encontrado = True # True, pois encontrou o valor
            break # Quebrando o loop pois o valor já foi encontrado.
        
    if not encontrado:
        print(f"O valor digitado {valor} não se encontra no vetor.")

if __name__ == '__main__':
    main()
    