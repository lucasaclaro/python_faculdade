vogais = {'aeiou'} #sem usar o construtor
vogais_2 = set('aeiouaaaaa') #construtor com string
vogais_3 = set(['a', 'e', 'i', 'o', 'u']) #construtor com lista
vogais_4 = set(('a', 'e', 'i', 'o', 'u')) #construtor com tupla

#a função set elimina os valores duplicados
print(vogais)
print(vogais_2)
print(vogais_3)
print(vogais_4)

print(set('banana')) #elimina os valores duplicados