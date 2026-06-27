

# Define uma função chamada 'sum' que recebe dois parâmetros: a e b
def sum(a, b):
    # Retorna o resultado da soma entre a e b para quem chamou a função
    return a + b

# Solicita ao usuário o primeiro número, converte o texto digitado para número inteiro (int) e guarda na variável 'a'
a = int(input("Enter first number: "))

# Solicita ao usuário o segundo número, converte para inteiro e guarda na variável 'b'
b = int(input("Enter second number: "))

# Exibe o resultado na tela usando uma f-string para formatar o texto
# Aqui, sum(a, b) chama a função criada lá no topo, passando os valores digitados
print(f'Sum of {a} and {b} is: {sum(a, b)}')