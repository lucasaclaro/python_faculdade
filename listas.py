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

frutas = ['maça', 'banana', 'uva', 'mamão', 'maça']
notas = [8.7, 5.2, 10, 3.5]

#in/not in - verificar um item em uma lista
print(f'Existe a fruta maça na lista?: {"maça" in frutas}.')
print(f'Existe a fruta abacate na lista?: {"abacate" in frutas}.')
print(f'Não existe a fruta abacate na lista?: {"abacate" not in frutas}.')

#min e max
print(f'Valor mínimo na lista de frutas: {min(frutas)}.')
print(f'Valor máxima na lista de notas: {max(notas)}.')

#count - contar o número de ocorrências
print(f'Quantas vezes a fruta maça aparece na lista?: {frutas.count("maça")}.')

#concatenar listas
print(f'Juntando as duas listas: {frutas + notas}.')

#Duplicar uma lista
print(f'Duplicando uma lista: {2 * frutas}.')


lista = ['Python', 30.61, 'Java', 51, ['a', 'b', 20], 'maça']

#len - tamanho da lista
print(f'Tamanho da lista: {len(lista)}.')

for indice, item in enumerate(lista):
    print(f'Posição {indice} \t Item: {item}.')

#slices - cortes nas lista
print(f'Lista [1]: {lista[1]}.')
print(f'Lista [0:2]: {lista[0:2]}.')
print(f'Lista [:2]: {lista[:2]}.')
print(f'Lista [3:]: {lista[3:]}.')
print(f'Lista [-2]: {lista[-2]}.')
print(f'Lista [4][1]: {lista[4][1]}.')

#List comprehension

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1

print(f'Lista antes da compressão: {linguagens}.')

linguagens = [item.lower() for item in linguagens]

print(f'Lista depois da compressão: {linguagens}.')

#Outra forma de fazer a compressão acima é utilizar o laço for
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

for indice, item in enumerate(linguagens):
    linguagens[indice] = item.lower()
print(f'Lista comprimida utilizando o laço for: {linguagens}.')


linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = [item for item in linguagens if "Java" in item]
print(f'Linguagens Java: {linguagens_java}.')

#A compressão acima também pode ser feita de outra maneira

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_com_java =[]
for item in linguagens:
    if "Java" in item:
        linguagens_com_java.append(item)
print(f'Linguagens Java: {linguagens_com_java}.')

