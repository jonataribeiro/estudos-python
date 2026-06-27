# ==============================================================================
# Python - Operadores Relacionais e Estruturas de Controle
# ==============================================================================
print()

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != diferente
# == igual

# Definição das variáveis numéricas para os testes relacionais
valorA = 20
valorB = 150
valorC = 30

print('valorA: ', valorA, 'valorB: ', valorB, 'valorC: ', valorC)
print()

# Operadores relacionais sempre retornam um valor booleano: True (Verdadeiro) ou False (Falso)
print('b é maior que a?', valorB > valorA)          # True, pois 150 > 20
print('b é menor que c?', valorB < valorC)          # False, pois 150 não é menor que 30
print('c é igual a 10?', valorC == 10)              # False, pois 30 não é igual a 10 (Nota: '==' compara, '=' atribui)
print('c é maior ou igual a b?', valorC >= valorB)  # False, pois 30 não é maior nem igual a 150
print('a é diferente de 20?', valorA != 20)          # False, pois 20 é igual a 20 (portanto, não é diferente)
print()


# ------------------------------------------------------------------------------
# IF | SE - Função de teste lógico (Estrutura Condicional)
# ------------------------------------------------------------------------------

# O 'if' avalia se a condição é verdadeira. Se for True, executa o bloco indentado logo abaixo.
if valorA > valorC:
    print('A é maior que C')
# O 'else' (senão) é executado automaticamente caso a condição do 'if' seja falsa (False).
else:
    print('C é maior que A')
print()


# ------------------------------------------------------------------------------
# While - Laço de Repetição (Loop baseado em condição)
# ------------------------------------------------------------------------------

# Reinicializa a variável valorA com o valor 1
valorA = 1

# O 'while' continuará repetindo o bloco de código abaixo ENQUANTO a condição (valorA <= 10) for Verdadeira
while valorA <= 10:
    print('Ciclo while: ', valorA)
    
    # Importante: Incrementa a variável em 1 a cada ciclo para que a condição um dia se torne Falsa.
    # Sem essa linha, o programa entraria em um "loop infinito".
    valorA += 1

print()