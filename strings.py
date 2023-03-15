texto = 'Aprendendo Python na disciplina de linguagem de programação.'

#len - tamanho do texto
print(f'Tamanho do texto: {len(texto)} caracteres.')

#in - procurar um caracter ou uma sequência de caracteres em um texto
print(f'Existe a palavra "Python" no texto: {"Python" in texto}.')

#count - quantidade de caracteres em um texto
print(f'Quantidade de vezes que a letra "y" aparece no texto: {texto.count("y")}.')

#sequência de caracteres
print(f'As cinco primeiras letras do texto são: {texto[0:6]}.')

#upper - letras em maísculas
print(f'O texto em letras maiúsculas fica assim: {texto.upper()}')

#lower - letras em minúsculas
print(f'O texto em letras minúsculas fica assim: {texto.lower()}')

#replace - substituir um caracter por outro
print(f'Substituir "y" por "XX" no texto: {texto.replace("y", "XX")}')

#split - cortar os textos e transformá-lo em uma lista. Caso não seja passado nenhum parâmetro, o texto é cortado em cada espaço em branco.
#Caso seja passado alguma parâmetro, por exemplo: texto.split(','), o texto será cortado nesse parâmetro.
palavras = texto.split()
print(f'Quantidade de palavras no texto: {len(palavras)}.')
texto_apoio = 'Aprendendo as linguagens de programação Python, Java, C, Javascript e outras.'
print(f'Fatiamento do texto pela ocorrência da vírgula: {texto_apoio.split(",")}.')

