import random

tam = int(input('Insira o tamanho da lista: '))
lista = []



for c in range(tam):
    lista.append(random.randint(1, tam))


print('\n--------- RESULTADO ---------\n')
for cu in lista:
    if cu % 3 == 0:
        print(f'{cu} - é\033[33m múltiplo de 3\033[m')
    if cu % 2 != 0:
        print(f'{cu} - é \033[31mimpar\033[m')
    else:
        print(f'{cu} - é \033[32mpar\033[m')
print('-----------------------------')