# Método é um procedimento que pode manipular atributos de objetos para qual o metódo foi criado. Em Python, métodos são funções que pertencem a um objeto e podem ser chamados usando a notação de ponto (objeto.método()).


print(type('Olá, mundo!'.upper))  # Converte todos os caracteres para maiúsculo
print('texto de exemplo'.capitalize())  # Converte o primeiro caractere para maiúsculo e os demais para minúsculo
print('TEXTO DE EXEMPLO'.lower())  # Converte todos os caracteres para minúsculo
print('texto de exemplo'.title())  # Converte o primeiro caractere de cada palavra para maiúsculo


# Concatenação de textos (strings)

textoA = 'Curso de Python'
textoB = ' - Aula 07'
textoC = 'Jônata Ribeiro'
Resultado = textoA + textoB + ' - ' + textoC
print(Resultado.upper())  # Concatena os textos
print('Tipo da variável Resultado:', type(Resultado))  # Exibe o tipo da variável Resultado
print()

varA, varB = 99, 199
print(varA + varB)  # Soma os valores das variáveis varA e varB
print()

varA, varB = 99, 199
print('Resultado da soma de varA e varB: ' + str(varA + varB))  # Soma os valores das variáveis varA e varB
print('Tipo da variável varA:', type(varA))  # Exibe o tipo da variável varA
print('Tipo da variável varB:', type(varB))  # Exibe o tipo da variável varB
print('Tipo da variável varA + varB:', type(varA + varB))  # Exibe o tipo da soma das variáveis varA e varB
print()


# Métodos para os textos (strings)

varTexto = 'Curso de Python - Aula 07'

# Preenchimento com caracteres à esquerda e à direita

print(varTexto.ljust(50, '*'))  # Preenche com '*' à esquerda
print(varTexto.rjust(50, '*'))  # Preenche com '*' à direita
print(varTexto.center(50, '*'))  # Preenche com '*' no centro
print()

print(varTexto.ljust(50, '-'))  # Preenche com '-' à esquerda
print(varTexto.ljust(50) + '|')  # Preenche com espaços à esquerda
print(varTexto.rjust(50, '-'))  # Preenche com '-' à direita
print(varTexto.center(50, '-'))  # Preenche com '-' no centro
print(varTexto.center(50) + '.')  # Preenche com espaços no centro
print(varTexto.center(50)) # Preenche com espaços no 
print()

# Repetições de caracteres

print('x' * 50)  # Repete o caractere 'x' 10 vezes
print('Python ' * 5)  # Repete a palavra 'Python' 5 vezes
print('Python ' * 5 + 'Aula 07')  # Repete a palavra 'Python' 5 vezes e concatena com 'Aula 07'
print('Python ' * 5 + 'Aula 07' + ' - Jônata Ribeiro')  # Repete a palavra 'Python' 5 vezes e concatena com 'Aula 07' e ' - Jônata Ribeiro'
print('Python ' * 5 + 'Aula 07' + ' - Jônata Ribeiro' + ' - Curso de Python')  # Repete a palavra 'Python' 5 vezes e concatena com 'Aula 07', ' - Jônata Ribeiro' e ' - Curso de Python'
print('Python ' * 5 + 'Aula 07' + ' - Jônata Ribeiro' + ' - Curso de Python' + ' - Aula 07')  # Repete a palavra 'Python' 5 vezes e concatena com 'Aula 07', ' - Jônata Ribeiro', ' - Curso de Python' e ' - Aula 07'
print()

# Alteração de caixa das palavras

varTexto = 'curso de python - aula 07'
print('Resultado do método capitalize():', varTexto.capitalize())  # Converte o primeiro caractere para maiúsculo e os demais para minúsculo
print('Resultado do método lower():', varTexto.lower())  # Converte todos os caracteres para minúsculo
print('Resultado do método upper():', varTexto.upper())  # Converte todos os caracteres para maiúsculo
print('jônata ribeiro'.title())  # Converte o primeiro caractere de cada palavra para maiúsculo
print()


print(varTexto.upper())  # Converte todos os caracteres para maiúsculo
print(varTexto.lower())  # Converte todos os caracteres para minúsculo

print('Resultado do método title():', varTexto.title())  # Converte o primeiro caractere de cada palavra para maiúsculo
print('Resultado do método upper():', varTexto.upper())  # Converte todos os caracteres
print()


# Função len (tamanho da string) e método count (contagem de caracteres


print(len(varTexto))  # Retorna o tamanho da string
print(varTexto.count('o'))  # Retorna a quantidade de vezes que a letra 'o' aparece na string
print(varTexto.count('curso'))  # Retorna a quantidade de vezes que a palavra 'curso' aparece na string
print(varTexto.count('python'))  # Retorna a quantidade de vezes que a palavra '
print()


print(len(varTexto))  # Retorna o tamanho da string
print(len('Jônata Ribeiro'))  # Retorna o tamanho da string
print(len('Curso de Python'))  # Retorna o tamanho da string
print()

# Extração de texto

print(varTexto)  # Exibe o conteúdo da string
print(varTexto[0:5])  # Exibe os caracteres do índice 0 ao 4
print(varTexto[6:11])  # Exibe os caracteres do índice 6 ao 10
print(varTexto[12:18])  # Exibe os caracteres do índice 12 ao 17
print(varTexto[19:24])  # Exibe os caracteres do índice 19 ao 

print(len(varTexto[0:5]))
print(varTexto[6])  # Exibe os caracteres do índice 6 até o final da string
print(varTexto[6:])  # Exibe os caracteres do índice 6 até o final da string
print(varTexto[:5])  # Exibe os caracteres do início da string até o índice 4
print(varTexto[:])  # Exibe todos os caracteres da string

# Eliminar espaços desnecessários no início e no final da string

varTexto = '   Curso de Python - Aula 07   '
print('Tamanho antes da limpeza', len(varTexto))  # Retorna o tamanho da string
print(varTexto.strip())  # Remove os espaços em branco do início e do final da string
print('Tamanho depois da limpeza', len(varTexto.strip()))  # Retorna o tamanho da string
print()


# Concatenar caracteres à sua string

varTexto = 'Curso de Python - Aula 07'
print('-'.join(varTexto))  # Adiciona o caractere '-' entre cada caractere da string
print(' '.join(varTexto))  # Adiciona o caractere ' ' entre cada caractere da string
print()
