"""
# Listas

# Criar a Lista

minhaLista = []
print(type(minhaLista))
print()

minhaLista = ['Curso', 'python', 'Trovato', 'YoutTube']
print(minhaLista)

# Tamanho da lista
print('Tamanho da lista:', len(minhaLista))

# Tipos de dados em listas

minhaLista2 = ['1', False, 'Trovato', 1.89766, minhaLista]
print(minhaLista2)


# Unificar listas

minhaLista2 = ['1', False, 'Trovato', 1.897866]
uniaoListas = minhaLista + minhaLista2
print(uniaoListas)

print()

# Duplicar os elementos de uma lista

listaDuplicada = minhaLista * 2
print(listaDuplicada)

print()

# Verificar os elementos de uma lista

print('Trovato' in minhaLista)

print('trovato' in minhaLista)

print()

# Trabalhar com listas

lstNumeros = [5, 10, 15, 20, 22, 25, 30, 55]

print('Mínimo:', min(lstNumeros))
print('Máximo:', max(lstNumeros))
print('Somatória:', sum(lstNumeros))
print()

# Métodos
# append

minhaLista.append('Valor Adicionado')
print(minhaLista)

# insert
minhaLista.insert(0, 'Primeiro Valor') # Na lista a Base começa sempre com 0
print(minhaLista)
print()

# pop - Elimina elementos da lista
minhaLista3 = ['Curso', 'python', 'Trovato', 'YoutTube']
print(minhaLista3)

print()

minhaLista3.pop() # o último registro
print(minhaLista3)

minhaLista3.pop(0) # o primeiro registros
print(minhaLista3)

# remove
minhaLista3.remove('Trovato')
print(minhaLista3)

print()

# sort | reverse
minhaLista3 = ['YouTube', 'Curso', 'Trovato', 'Python', 'Aula 12']
print(minhaLista3)

minhaLista3.sort()
print(minhaLista3)

minhaLista3.reverse()
print(minhaLista3)

minhaLista3 = minhaLista3 * 3
print('Qtd.Python:', minhaLista3.count('Python'))
print('Qtd.VBA:', minhaLista3.count('VBA'))

print()


# retornar
print(minhaLista3[1])
print()
"""



# ==============================================================================
# 📝 MEU RESUMÃO DE ESTUDOS: TUDO SOBRE LISTAS EM PYTHON
# ==============================================================================

# 📌 1. O BÁSICO: CRIAR, TAMANHO E TIPOS DE DADOS
# ------------------------------------------------------------------------------
# - Criar lista vazia: uso colchetes [] ou a função list().
# - Descobrir o tamanho: uso len(nome_da_lista). Super útil para loops!
# - Tipos de dados: No Python, a lista é "mãe de todos". Posso misturar tudo
#   dentro dela: Texto (str), Inteiro (int), Decimal (float), Booleano (True/False)
#   e até colocar uma lista dentro de outra lista!

minhaLista = ['Curso', 'python', 'Trovato', 'YoutTube']
print('Elementos:', minhaLista, '| Qtd:', len(minhaLista))


# 📌 2. TRUQUES COM OPERADORES (+ e *)
# ------------------------------------------------------------------------------
# - Juntar duas listas (Unificar): basta usar o sinal de +. Ele cria uma lista nova.
# - Duplicar os elementos: se eu multiplicar a lista por um número (ex: lista * 2),
#   o Python não multiplica os números de dentro, ele CLONA os elementos em sequência.

lista_A = [1, 2]
lista_B = [3, 4]
print('União (+):', lista_A + lista_B)
print('Clone (*):', lista_A * 3)


# 📌 3. PROCURAR COISAS NA LISTA (Operador 'in')
# ------------------------------------------------------------------------------
# - O operador 'in' verifica se algo está na lista e responde True ou False.
# - ATENÇÃO: O Python é "Case Sensitive" (diferencia maiúsculas de minúsculas).
#   'Trovato' in lista vai dar True, mas 'trovato' (com t minúsculo) vai dar False!

print('Tem Trovato?', 'Trovato' in minhaLista)


# 📌 4. MATEMÁTICA RÁPIDA (Funções Nativas)
# ------------------------------------------------------------------------------
# - Se a lista for só de números, o Python resolve minha vida com 3 funções:
#   min() -> acha o menor número.
#   max() -> acha o maior número.
#   sum() -> soma todo mundo automaticamente.

numeros = [5, 10, 15]
print('Menor:', min(numeros), '| Maior:', max(numeros), '| Total:', sum(numeros))


# 📌 5. COLOCAR COISAS NA LISTA (Métodos de Adição)
# ------------------------------------------------------------------------------
# - .append('valor'): Joga o elemento direto no FIM da lista. É o que mais uso!
# - .insert(indice, 'valor'): Coloca o elemento onde eu mandar. 
#   Lembrando: A contagem de posições (índices) no Python SEMPRE começa no ZERO.

minhaLista.append('Fim')
minhaLista.insert(0, 'Início') # Ocupa a posição 0 e empurra o resto para frente


# 📌 6. TIRAR COISAS DA LISTA (Métodos de Remoção)
# ------------------------------------------------------------------------------
# - .pop(): Sem passar nada, ele remove e joga fora o ÚLTIMO elemento da lista.
# - .pop(0): Se eu passar a posição, ele remove o elemento daquela posição específica.
# - .remove('Valor'): Aqui eu não passo a posição, eu passo o NOME do que quero apagar.
#   Se o elemento não existir, o Python dá erro, então cuidado.

teste_remover = ['A', 'B', 'C']
teste_remover.pop()       # Apaga o 'C'
teste_remover.remove('A') # Apaga o 'A'


# 📌 7. ORGANIZAÇÃO E CONTAGEM (Métodos Extras)
# ------------------------------------------------------------------------------
# - .sort(): Organiza a lista. Se for texto, deixa em ordem alfabética. Se for número, em ordem crescente.
# - .reverse(): Inverte a lista de trás para frente.
# - .count('Valor'): Conta quantas vezes aquele termo exato aparece dentro da lista.

dados = ['B', 'A', 'C']
dados.sort() # Vira ['A', 'B', 'C']


# 📌 8. PEGAR UM ELEMENTO ESPECÍFICO (Índices)
# ------------------------------------------------------------------------------
# - Para exibir ou usar só um pedaço da lista, uso o nome dela com a posição em colchetes.
# - Exemplo: minhaLista[1] vai pegar o SEGUNDO elemento (já que o primeiro é o 0).

print('O segundo elemento é:', minhaLista[1])