saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b




def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'soma':
        return adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        return subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        return multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        return divisao(num1, num2)
    else:
        return "Operação inválida"




while saida.lower() != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, / ou nome da operação): ")
    resultado = calculadora(num1, num2, operacao)

    print('Resultado da operação:', resultado)
    
    saida = input("Deseja continuar (S/N)? ")
print("Programa encerrado.")