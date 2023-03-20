import random

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

lista = random.sample(range(1000), 50)
print(sorted(lista))
print(executar_busca_linear(lista, 10))




lista = ['a', 'e', 'i', 'o', 'u']

def procurar_valor(lista, valor):
    tamanho_da_lista = len(lista)
    for indice in range(tamanho_da_lista):
        if valor == lista[indice]:
             return f'O valor {valor} está na posição {indice}.'
    return None
print(lista)
print(procurar_valor(lista, 'a'))

for indice, valor in enumerate(lista):
    print(f'Índice {indice} \t Valor: {valor}.')


print(lista.index('a'))