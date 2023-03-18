#As estruturas de dados que possuem um mapeamento entre uma chave e um valor são consideradas objetos do tipo mapping (dicionários)

#Formas de criar um dicionário

dici_um = {}
dici_um['nome'] = 'João'
dici_um['idade'] = 30

dici_dois = dict([('nome', 'João'), ('idade', 30)])

dici_tres = {'nome': 'João', 'idade': 30}



print(dici_um)
print(dici_dois)
print(dici_tres)


#Formar de acessar um dicionário
print(dici_um['nome'])

cadastro = {
            'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
            'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
            'idade' : [25, 33, 37, 18]
            }

print(cadastro['nome'])

print(cadastro['nome'][2])

print(cadastro.keys())

print(cadastro.values())

print(cadastro.items())

print(len(cadastro['nome']))
