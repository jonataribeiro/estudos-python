# ==============================================================================
# VARIÁVEIS, ESCOPO E FUNÇÃO RANGE
# ==============================================================================

print()

# ------------------------------------------------------------------------------
# Seção 1: Tipos Primitivos de Dados
# ------------------------------------------------------------------------------
# O Python possui tipagem dinâmica. Ele descobre o tipo do dado baseado no valor que você atribui.

varA = 10         # int (Número Inteiro)
varB = 'Emerson'  # str (String / Texto)
varC = False      # bool (Booleano: Apenas True ou False. Sempre com inicial maiúscula!)
varD = 1.34567    # float (Número Decimal / Ponto Flutuante)

# Coerção Automática: Quando somamos um 'int' com um 'float', o Python transforma o resultado em 'float'
varE = varA + varD 

# O comando type() exibe a classe/tipo de cada uma das variáveis acima
print(type(varA), type(varB), type(varC), type(varD), '\nResultado:', varE)
print()


# ------------------------------------------------------------------------------
# Seção 2: Escopo de Variáveis (Global vs Local)
# ------------------------------------------------------------------------------
# Escopo determina ONDE uma variável existe e pode ser usada no seu programa.

def Funcao1(a):
    # 'a' é um parâmetro (Escopo Local: só existe dentro desta função).
    # 'varF' é uma variável do Escopo Global (criada fora da função, acessível em qualquer lugar).
    print(a + varF)

def Funcao2(a):
    # 'varG' é uma variável de Escopo Local. Ela nasce e morre dentro da Funcao2.
    # Se você tentar dar um print(varG) fora da função, o Python vai dar um erro dizendo que ela não existe.
    varG = 100
    print(a * varF + 100)

# O programa principal começa de verdade aqui embaixo:
# O input recebe um texto e o int() o transforma em número inteiro global.
varF = int(input('Digite um número inteiro: '))

# Chamando as funções e passando valores que vão preencher o parâmetro 'a'
Funcao1(25)   # Executa: 25 + varF
Funcao2(100)  # Executa: 100 * varF + 100

print()


# ------------------------------------------------------------------------------
# Seção 3: A Função Range (Geradora de Intervalos)
# ------------------------------------------------------------------------------
# O range() cria uma sequência de números. Ele é muito usado com laços 'for'.
# Regra de Ouro do Mentor: O início é INCLUSIVO, mas o fim é EXCLUSIVO (ele para um número antes).

# Se passarmos apenas 1 argumento, ele assume que começa no 0 e vai até o (número - 1)
varH = range(4) # Gera a lógica dos números: 0, 1, 2, 3
print(type(varH)) # O tipo dele é a classe 'range'

# Para visualizar os números do range na tela como uma lista, precisamos convertê-lo usando list()
print(list(varH))

# range(início, fim) -> Começa no 2 e para no 9 (o 10 fica de fora)
print(list(range(2, 10))) 

# range(início, fim, passo) -> Começa no 2, vai até o 9, pulando de 2 em 2
print(list(range(2, 10, 2)))

# range com passo negativo (Regressivo) -> Começa no 2, vai descendo de -1 em -1 até chegar no -9 (o -10 fica de fora)
print(list(range(2, -10, -1)))