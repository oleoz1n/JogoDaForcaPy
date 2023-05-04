palavra = input("Qual a palavra secreta?: ").upper()
qtdChances = int(input("Qual a quantidade de chances?: "))
AaZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letrasUsadas = []
print('\n'*20)
forca = []
x = 0
array_palavra = []

for n in palavra:
    array_palavra += n
for n in range(len(palavra)):
    forca += "_"
for n in range(len(forca)):
    print(forca[n],end = ' ')

for n in range(qtdChances,0,-1):
    y = 0
    for ni in forca:
        if ni == '_':
            y+=1
    if y > 0:
        print(f'\n\nVocê tem {n} tentativas')

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
        for n in array_palavra:
            if chute == n:
                forca.pop(x)
                forca.insert(x, n)
            x += 1
        x = 0
        for n in range(len(forca)):
            print(forca[n], end=' ')
    else:
        break
y = 0
for ni in forca:
    if ni == '_':
        y+=1
if y == 0:
    print('\n\nParabéns você acertou!!!')
else:
    print('\n\nvocê perdeu ;-;')