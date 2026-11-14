meta = 8000

while True:
    try:
        passos_feitos = int(input("Digite a quantidade de passos realizados: "))
        if passos_feitos < 0:
            print("Por favor, digite um número positivo.")
        elif passos_feitos == meta:
            print(f'Parabéns! Você bateu a meta exata de {meta} passos.')
            break 
        elif passos_feitos > meta:
            passos_excedentes = passos_feitos - meta
            print(f'Parabéns! Você excedeu a meta em {passos_excedentes} passos.')
            break 
        else:
            passos_faltantes = meta - passos_feitos
            print(f'Você não bateu a meta.\nVocê ainda precisa de {passos_faltantes} passos para atingir a meta de {meta} passos.')
            break
    except ValueError:
        print("Por favor, digite um número válido.")

