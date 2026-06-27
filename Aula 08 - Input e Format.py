# ==============================================================================
# Python - Entrada de Dados (Input) e Formatação de Strings
# ==============================================================================

# Input - Obter dados do usuário
# A função input() permite que o usuário insira dados no programa.

# Exemplo de uso da função input() (O bloco abaixo está comentado com docstring, servindo de histórico)
"""
print()

varNome = input("Digite o seu nome: ")
print("Olá,", varNome + "!\nSeja bem-vindo(a)!")

print()

varNome = input("Digite o seu nome: ")
print("Olá, " + varNome + "!\nSeja bem-vindo(A)!")
"""

print()

# Importa a biblioteca matemática 'math' dando a ela o apelido (alias) de 'm'
import math as m

# Captura o nome do usuário. Lembre-se: o input() sempre devolve o dado como Texto (String)
varNome = input('Digite o seu nome: ')
print('Olá,', varNome + '!\n')

print('Calcular a área de uma circunnferência: ')

# Captura o raio. Como vem em formato de texto, precisaremos converter depois
varRaio = input('Informe o raio da circunferência: ') # input do raio

# m.pi puxa o valor exato de Pi (3.14159...). 
# float(varRaio) converte o texto do raio em número decimal para que o cálculo aconteça
varResultado = m.pi * float(varRaio) ** 2
print('Área:', varResultado)
print('Comprimento:', 2 * m.pi * float(varRaio))
print()

# ------------------------------------------------------------------------------
# 2º exemplo: Converter graus Celsius para Fahrenheit
# ------------------------------------------------------------------------------

# Aqui a conversão para float() é feita diretamente na mesma linha do input()
varTemperatura = float(input('Digite o valor em Celsius: '))
varResultado = (varTemperatura * 1.8) + 32
print('Farenheith:', varResultado)
print('-' * 50)

# ------------------------------------------------------------------------------
# Método format - Substituição usando índices {0}, {1}, {2}
# ------------------------------------------------------------------------------

# O {0} indica que a primeira variável passada no .format() será encaixada ali
varTexto = '{0}, seja bem-vindo(a)!'
print(varTexto.format(varNome))
print()

varIdade = 51
varProfissao = 'Analista de Treinamento na MLF'

# Os números dentro das chaves {0}, {1}, {2} correspondem à ordem exata das variáveis no .format()
varTexto = '{0}, seja bem-vindo(a)! \nIdade: {1} \nProfissão: {2}'
print(varTexto.format(varNome, varIdade, varProfissao))
print()

# Repetição dos cálculos de circunferência para fins de comparação com a formatação abaixo
varResultado = m.pi * float(varRaio) ** 2
print('Área:', varResultado)
print('Comprimento:', 2 * m.pi * float(varRaio))
print()

# ------------------------------------------------------------------------------
# Formatar o resultado (Limitação de Casas Decimais)
# ------------------------------------------------------------------------------

# O código {0:.1f} diz: pegue o primeiro argumento (índice 0) e mostre apenas 1 casa decimal (.1f)
# Nota de estudo: No seu código original constava "ºC" no texto, mas o cálculo acima era sobre a Área.
Res_Final = 'Área: {0:.1f} ºC' 
print(Res_Final.format(varResultado))
print()