nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
cidade = input("Digite sua cidade: ")

print(f'Tipo Nome:{type(nome).__name__}\nTipo Idade:{type(idade).__name__}\nTipo Altura:{type(altura).__name__}\nTipo Cidade:{type(cidade).__name__}')
print("\n")
print(f'Olá {nome}! Você tem {idade} anos, mede {altura}m e mora em {cidade}.')