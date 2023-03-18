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

#O poder do objeto set está em suas operações matemáticas de conjuntos.
# Vejamos um exemplo: uma loja de informática recebeu componentes usados de um computador para avaliar se estão com defeito.
# As peças que não estiverem com defeito podem ser colocadas à venda. Como, então, podemos criar uma solução em Python para resolver esse problema?
# A resposta é simples: usando objetos do tipo set. Observe o código a seguir.

def create_report():
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora',
     'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura','placa de som', 'placa de vídeo', 'placa mãe',
     'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")

    print("Os componentes que podem ser vendidos são:")
    for item in componentes_ok:
        print(item)

create_report()


#Outro exemplo

def numeros_diferentes_caixas():
    numeros_caixa_um = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    numeros_caixa_dois = set([1, 5, 7])

    numeros_diferentes = numeros_caixa_um.difference(numeros_caixa_dois)

    print(f'Os números da caixa um são: {numeros_caixa_um} e da caixa dois são: {numeros_caixa_dois}.\n'
          f'Os números que não se repetem entre as duas caixas são: {numeros_diferentes}.')

numeros_diferentes_caixas()