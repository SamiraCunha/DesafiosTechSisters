# Criar um algoritmo ou função que solicite um número ao usuário e verifique se o valor é positivo, negativo ou nulo (zero).

numero = int(input("Insira o número: "))

if numero == 0:
    print(f'O número {numero} é nulo')

elif numero > 0:
    print(f'O número {numero} é positivo' )
elif numero < 0:
    print(f'O número {numero} é negativo')
else:
    print("Digite apenas números")
