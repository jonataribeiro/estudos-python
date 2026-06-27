# ==============================================================================
# MENTORIA PYTHON: OPERADORES DE ASSOCIAÇÃO E LÓGICOS
# ==============================================================================

print()

# Cria um intervalo que vai de 1 até 5 (lembre-se: o 6 fica de fora!)
x = range(1, 6)

# ------------------------------------------------------------------------------
# Seção 1: Operadores de Associação (Pertencimento)
# ------------------------------------------------------------------------------
# Servem para verificar se um elemento está ou não dentro de uma coleção/sequência.

print('********** Operador in **********')
print('1 em x..........:', 1 in x)       # True: O número 1 está no intervalo [1, 2, 3, 4, 5]
print('99 em x..........:', 99 in x)     # False: O número 99 não está no intervalo

# ⚠️ PEGADINHA DE ESTUDO: 
# Aqui o Python avalia primeiro o '1' (que em lógica é considerado verdadeiro/True por não ser zero)
# E depois avalia se '99 in x' (que é False). Por isso, o resultado final pode ser confuso no terminal.
# Para testar se ambos estão na lista, o correto seria: (1 in x) and (99 in x)
print('1 e 3 em x.....', 1 and 99 in x)

print()

print('********** Operador in **********')
# 'not in' funciona de forma inversa: ele pergunta "É verdade que este número NÃO está aqui?"
print('1 not in x...:', 1 not in x)    # False: Porque o 1 ESTÁ lá dentro.
print('99 not in x..:', 99 not in x)   # True: Porque o 99 realmente NÃO está lá dentro.

# ⚠️ OUTRA PEGADINHA:
# Mesma regra anterior. O Python avalia o '1' isolado primeiro, e depois o resto da expressão.
print('1 and 3 not in x:', 1 and 3 not in x)

print()

# ------------------------------------------------------------------------------
# Seção 2: Operadores Lógicos (Tabelas Verdade)
# ------------------------------------------------------------------------------
# Servem para conectar e avaliar múltiplas condições ao mesmo tempo.

num1 = 3
num2 = 6
num3 = 9

print('num1=', num1, 'num2=', num2, 'num3=', num3)
print()

# Operador AND (E): Exige que TODAS as condições sejam verdadeiras para dar True.
# Condição 1: (3 > 6) é Falsa. Condição 2: (6 > 9) é Falsa. 
print('num1 é maior do que num2 E num2 é maior que num3?', num1 > num2 and num2 > num3) # Retorna False

# Condição 1: (9 > 6) é Verdadeira. Condição 2: (6 > 3) é Verdadeira.
# Como ambas são True, o resultado final é True.
print('num3 é maior do que num2 E num2 é maior que num1?', num3 > num2 and num2 > num1) # Retorna True
print()

# ------------------------------------------------------------------------------
# Seção 3: O Operador NOT (Negação / Inversor)
# ------------------------------------------------------------------------------
# O 'not' simplesmente inverte o estado lógico de qualquer coisa.

print(not(False))  # Inverte Falso para -> True
print(not(True))   # Inverte Verdadeiro para -> False

# Primeiro o Python resolve o que está dentro dos parênteses: (1 == 2) é Falso.
# Depois o 'not' inverte esse resultado de Falso para -> True.
print(not(1 == 2))