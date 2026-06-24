# Tipos de Dados em Python
# Aula 06 - Variáveis

# int, float, str, bool, list, tuple, set, 

# Tipos primitivos de dados em Python:

# int: números inteiros, positivos ou negativos, sem casas decimais
# float: números reais, positivos ou negativos, com casas decimais
# string: sequência de caracteres, delimitada por aspas simples ou duplas
# bool: valores booleanos, True ou False
# complex: números complexos, com parte real e imaginária, delimitados por j ou J

# list: lista de elementos, delimitada por colchetes, podendo conter elementos de tipos diferentes
# tuple: tupla de elementos, delimitada por parênteses, podendo conter elementos de tipos diferentes, mas imutável
# set: conjunto de elementos, delimitado por chaves, não permite elementos duplicados
# dict: dicionário de elementos, delimitado por chaves, contendo pares de chave e valor


# Variáveis de texto

texto = 'Curso de Python'
print(texto)
print('Tipo da variável texto:', type(texto))
print()

varNumero = '123'
print(varNumero)
print('Tipo da variável varNumero:', type(varNumero))


# Variáveis para tipos numéricos

varA = 10
varB = 20.5
varC = False
varD = 3 + 4j
varE = 'Python: Olá, mundo!'

print(varA, varB, varC, varD, varE)
print()

print('Tipo da variável varA:', type(varA))
print('Tipo da variável varB:', type(varB))
print('Tipo da variável varC:', type(varC))
print('Tipo da variável varD:', type(varD))
print('Tipo da variável varE:', type(varE))

print(type(varA), type(varB), type(varC), type(varD), type(varE))
print()

# Conversão de tipos de dados

varF = float(varA)  # Converte varA para float
print('Float de varF:', type(varF))
print()

varG = int(varB)  # Converte varB para int
print('Int de varG:', type(varG))
print(varG)
print()


# Variáveis booleanas

varH = False
varI = True
varJ = not(False)  # Converte False para True
varK = not(True)   # Converte True para False

print(varH, varI, varJ, varK)
print()

