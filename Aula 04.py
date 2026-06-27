# ==============================================================================
# Python - Aula 04 - Comentários e Print
# ==============================================================================

# Declaração de uma variável simples. O '#' inicia um comentário de linha única.
a = 1  # variável de exemplo para comentários

# docstring - Usadas para documentação multilinha (geralmente dentro de funções/classes)

"""
    Este é um comentário
    que ocupa várias linhas
    usando três aspas duplas.
"""

'''
    Que também pode ser
    com aspas simples
    (três aspas simples seguidas).
'''

# O print() vazio serve apenas para pular uma linha na tela do terminal
print()

# Demonstração do uso de aspas simples por fora e aspas duplas por dentro
print("Se você pretende mesclar 'símbolos' diferentes, então você pode usar aspas simples e duplas, como no exemplo acima.")

# Demonstração inversa: aspas duplas por fora e aspas simples por dentro
print('Ou isso, "para alternar" entre aspas simples e duplas.')
print()


# ------------------------------------------------------------------------------
# Seção: print e seus argumentos (sep, end, file)
# ------------------------------------------------------------------------------

# Print simples de uma string de texto
print('Teste de saída')

# O caractere de escape '\n' força uma quebra de linha no meio do texto
print('Teste de saída \nem várias linhas')

# Passando múltiplos argumentos separados por vírgula (por padrão, o Python adiciona um espaço entre eles)
print('Curso', 'de', 'Python')

# O argumento 'sep' altera o separador padrão (espaço) para o caractere escolhido (neste caso, '-')
# O argumento 'end' altera o comportamento final (por padrão ele quebra a linha, aqui ele deixa apenas um espaço ' ')
print('Curso', 'de', 'Python', sep='-', end=' ')    # separar as partes utilizando o separador "-" e não quebrar a linha no final

# Como o print anterior não quebrou a linha, este texto começa logo em seguida
# O argumento 'end="."' faz com que a linha termine com um ponto final em vez de quebrar a linha automaticamente
print('Curso', 'de', 'Python', end='.')             # finaliza a string com