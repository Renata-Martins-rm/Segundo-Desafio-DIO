while True:

    vitoria = int(input('Qual a quantidade de vitórias do seu Herói? '))
    derrota = int(input('Qual a quantidade de derrotas do seu Herói? '))

    def rankear(vitoria, derrota):
        resultado = vitoria - derrota    
        return resultado
    saldoVitorias = rankear(vitoria, derrota)

    if saldoVitorias <= 10:
        nivel = 'Ferro'
    elif saldoVitorias <= 20:
        nivel = 'Bronze'
    elif saldoVitorias <= 50:
        nivel = 'Prata'
    elif saldoVitorias <= 80:
        nivel = 'Ouro'
    elif saldoVitorias <= 90:
        nivel = 'Diamante'
    elif saldoVitorias <= 100:
        nivel = 'Lendário'
    else: 
        nivel = 'Imortal'

    print(f'O Herói tem o saldo de {saldoVitorias} pontos e está no nível {nivel}!')

    resp = input('Deseja continuar? [S/N] ').upper()
    if resp != 'S':
        print("Fim!")
        break

