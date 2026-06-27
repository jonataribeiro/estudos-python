
# DocString - Uma string especial usada para documentar o que o código faz

def minhaFuncao(parametro1, parametro2, parametro3):
    """
    Descrição da função:
    Esta função realiza uma operação simples com três parâmetros.

    Parâmetros:
    parametro1 (tipo): Descrição do primeiro parâmetro.
    parametro2 (tipo): Descrição do segundo parâmetro.
    parametro3 (tipo): Descrição do terceiro parâmetro.

    Retorna:
    tipo: Descrição do valor retornado.
    """
    # Implementação da função
    # resultado = parametro1 + parametro2 + parametro3  # Exemplo de operação
    # return resultado

    # O comando type() descobre e exibe o tipo de dado de cada variável
    # O print vai mostrar na tela esses tipos lado a lado
    print(type(parametro1), type(parametro2), type(parametro3))

# Chamada da função passando três tipos de dados diferentes:
# 'Alessandro' é uma String (str)
# 51 é um número Inteiro (int)
# [1, 2, 3] é uma Lista (list)
minhaFuncao('Alessandro', 51, [1, 2, 3])