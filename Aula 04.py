# Python
# Aula 04 - Comentários

a = 1 # variável de exemplo para comentários

# docstring

"""
    Este é um comentário
    que ocupa várias linhas

"""

'''
    Que também pode ser
    com aspas simples
'''

print()
print("Se você pretende mesclar 'símbolos' diferentes, então você pode usar aspas simples e duplas, como no exemplo acima.")
print('Ou isso, "para alternar" entre aspas simples e duplas.')
print()


# print

print('Teste de saída')
print('Teste de saída \nem várias linhas')
print('Curso', 'de', 'Python')
print('Curso', 'de', 'Python', sep='-', end=' ')    # separar as partes utilizando o separador "-" e não quebrar a linha no final
print('Curso', 'de', 'Python', end='.')             # finaliza a string com um determinado caractere, no caso o ponto final
print()
print('Curso \t de \t Python')                      # separador de tabulação

arquivo = open('Aula 04 - saída.txt', 'a+')  # abre o arquivo para escrita, caso não exista ele será criado

print('Curso', 'de', 'Python', file=arquivo)  # escreve no arquivo
arquivo.close()  # fecha o arquivo

print()
