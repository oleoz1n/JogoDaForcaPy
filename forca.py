palavra = input("Qual a palavra secreta?: ").upper()
qtdChances = int(input("Qual a quantidade de chances?: "))
perfect = qtdChances
AaZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letrasUsadas = []
print('\n'*20)
forca = []
array_palavra = []

for n in palavra:
    array_palavra += n
for n in range(len(palavra)):
    forca += "_"
for n in range(len(forca)):
    print(forca[n],end = ' ')

while qtdChances > 0:
    y = 0
    for ni in forca:
        if ni == '_':
            y+=1
    if y > 0:
        print(f'\n\nVocê tem {qtdChances} tentativas')
        while True:
            if len(letrasUsadas) > 0:
                for a in letrasUsadas:
                    print(a, end=' ')
                print('essas letras já foram usadas.')
            quebra = 0
            chute = input("Qual letra acha que tem?: ").upper()
            for i in AaZ:
                if i == chute:
                    quebra += 1
            if quebra > 0:
                letrasUsadas.append(chute)
                break
            print('Essa letra ja foi usada.\n')
        AaZ.remove(chute)
        z = 0
        x = 0
        for n in array_palavra:
            if chute == n:
                forca.pop(x)
                forca.insert(x, n)
                z += 1
            x += 1
        if z > 0:
            qtdChances += 1
        for n in range(len(forca)):
            print(forca[n], end=' ')
    else:
        break
    qtdChances -= 1
y = 0
for ni in forca:
    if ni == '_':
        y+=1
if y == 0:
    if qtdChances == perfect:
        print('\n\nTa de hack, não errou uma meu mano!')
    else:
        print('\n\nParabéns você acertou!!!')
        print(f'Restavam {qtdChances} chances')
else:
    print(f'\n\nA palavra era: {palavra}\nvocê perdeu ;-;')
