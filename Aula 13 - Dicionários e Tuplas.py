# ==============================================================================
# MENTORIA PYTHON: TUPLAS E DICIONÁRIOS
# ==============================================================================

# ------------------------------------------------------------------------------
# Seção 1: Tuplas (Sequências Imutáveis)
# ------------------------------------------------------------------------------
# Diferença crucial: Listas [ ] podem mudar. Tuplas ( ) NUNCA mudam após criadas.
print()

# Uma tupla pode ser criada com ou sem parênteses, basta separar os itens por vírgula
tupla1 = 'a', 'd', 1, 2, {1,2,3}
tupla2 = ('a', 'd', 1, 2, {1,2,3})

print(tupla1, '\n', tupla2)
print(type(tupla1), '\n', type(tupla2)) # Ambas serão da classe 'tuple'

# ⚠️ REGRA DE OURO: A linha abaixo daria erro (TypeError), pois não podemos alterar itens de uma tupla
# tupla1[1] = 'Atualizar'

# ⚠️ CUIDADO: Se você colocar só um texto, o Python acha que é uma String comum (str)
tupla3 = 'Emerson'
print(type(tupla3)) 
# Dica do Mentor: Para criar uma tupla de um elemento só, use uma vírgula no final: tupla3 = 'Emerson',

# Criando uma tupla vazia
tupla4 = ()
print(tupla4)

# ⚠️ Outro erro: Não dá para adicionar elementos dinamicamente em uma tupla vazia. Use listas se precisar disso!
# tupla4[0] = 'Emerson'     
# print(tupla4)

# A função tuple() transforma um iterável em tupla. Strings são fatiadas caractere por caractere.
tupla5 = tuple("abc") # Vira ('a', 'b', 'c')
print(type(tupla5))

print()
print('-' * 30)
print()


# ------------------------------------------------------------------------------
# Seção 2: Dicionários (Estruturas Chave-Valor)
# ------------------------------------------------------------------------------
# Em vez de índices numéricos (0, 1, 2), os dicionários usam Chaves personalizadas para guardar Valores.

print('Dicionários')

# Criamos usando chaves { }. No exemplo: 1 e 2 são as CHAVES; 'Emerson' e 'Márcia' são os VALORES.
dicionarioA = {1: 'Emerson', 2: 'Márcia'}
print(dicionarioA)
print(type(dicionarioA)) # Classe 'dict'

# len() em dicionários conta quantos pares de (Chave: Valor) existem lá dentro
print(len(dicionarioA))

# Adicionar valores: Basta indicar o nome do dicionário, a nova chave entre colchetes e atribuir o valor
dicionarioA[3] = 'Paula'
dicionarioA[4] = 'Maria Carla'
print(dicionarioA)

# Método .update(): Serve para atualizar o valor de chaves que já existem (ou adicionar novas)
dicionarioA.update({1: 'Novo instrutor'}) # Substitui 'Emerson' por 'Novos