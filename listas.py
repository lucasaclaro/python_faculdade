#Listas são mutáveis

lista_vogais = ['a', 'e', 'i', 'o', 'u']

#percorrer uma lista com a função index para saber a posição de cada elemento
for vogal in lista_vogais:
    print(f'Posição: {lista_vogais.index(vogal)}, Vogal: {vogal}')

#enumerate - para retornar a posição de um elemento em uma lista também pode ser utilizada essa função
for posicao, vogal in enumerate(lista_vogais):
    print(f'Posição: {posicao}, Vogal: {vogal}')



#append - adicionar elementos ao final de uma lista
lista_vogais.append('g')
print(lista_vogais)