def menu_jogo(): #Esse procedimemto tem o objetivo de saber se o usuário quer continuar jogando.
    while True:
        print('''
[1]Continuar jogando
[0]Sair do jogo''')
        resp = input(": ")
        print('\n')
        if resp == '1':
            jogo_forca()
        elif resp == '0':
            break
        
def jogo_forca():
    invalid = [] #captura os caracteres inválidos da palavra
    palavra = input("Qual a palavra secreta?: ").upper()
    qtd_chances = int(input("Qual a quantidade de chances?: "))
    perfect = qtd_chances # caso o usuário não erre nenhuma letra, tem um easter egg
    AaZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Ç'] # Todas as letras possíveis de serem usadas.
    aReplace = ['Á', 'À', 'Ã', 'Â'] # Serve para tirar os acentos das letras.
    eReplace = ['É', 'È', 'Ê'] # Serve para tirar os acentos das letras.
    iReplace = ['Í', 'Ì', 'Î'] # Serve para tirar os acentos das letras.
    oReplace = ['Ó', 'Ò', 'Õ', 'Ô'] # Serve para tirar os acentos das letras.
    uReplace = ['Ú', 'Ù', 'Û'] # Serve para tirar os acentos das letras.
    letras_usadas = [] # será preenchido com as letras que o usuário já usou
    print('\n'*20)
    forca = [] # array com '_' no lugar das letras
    array_palavra = [] # é a palavra só que em array

    for n in palavra:
        array_palavra += n
    letra = 0
    for n in array_palavra: # Serve para tirar os acentos das letras.
        if n in aReplace:
            array_palavra[letra] = 'A'
        if n in eReplace:
            array_palavra[letra] = 'E'
        if n in iReplace:
            array_palavra[letra] = 'I'
        if n in oReplace:
            array_palavra[letra] = 'O'
        if n in uReplace:
            array_palavra[letra] = 'U'
        letra += 1
    erro = 0
    for n in array_palavra: # Serve para ver se a palavra tem caracteres inválidos como: ';' '.' ',' ':' '/' '|' '\' ...
        if n in AaZ:
            pass
        else:
            invalid.append(n)
            erro += 1
    if erro > 0: #abre o menu caso a palavra tenha um caractere inválido
        print(f'{invalid} Caracter inválido')
        menu_jogo()
        exit()
    for n in range(len(palavra)): #troca as letras por '_'
        forca += "_"
    for n in range(len(forca)): #printa a forca
        print(forca[n],end = ' ')
    while qtd_chances > 0: #a advinhação da palavra
        qtd_segredos = 0 
        for segredo in forca:
            if segredo == '_':
                qtd_segredos+=1
        if qtd_segredos > 0: #executa o código enquanto todas as letras ainda não foram chadas
            print(f'\n\nVocê tem {qtd_chances} tentativas')
            while True: #executa enquanto o usuário não digita uma letra que não tem no array
                quebra = 0 #caso a letra n seja repetida ele soma +1 e quebrea o while
                if len(letras_usadas) > 0:
                    for a in letras_usadas:
                        print(a, end=' ')
                    print('essas letras já foram usadas.')
                chute = input("Qual letra acha que tem?: ").upper()
                for i in AaZ:
                    if i == chute:
                        quebra += 1
                if quebra > 0:
                    letras_usadas.append(chute)
                    break
                print('Essa letra ja foi usada.\n')
            AaZ.remove(chute) # remove as letras usadas da array de todas as letras possíveis
            letra_certa = 0 # confere se o usuário acertou a letra
            num_forca = 0 # confere qual onjeto do array forca está dentro do if
            for n in array_palavra:
                if chute == n:
                    forca.pop(num_forca)
                    forca.insert(num_forca, n)
                    letra_certa += 1
                num_forca += 1
            if letra_certa == 0:
                qtd_chances -= 1 #caso o usuário acerta a letra a quantidades de chance continua a mesma
            for n in range(len(forca)):
                print(forca[n], end=' ')
        elif qtd_segredos == 0:
            break
    if qtd_chances == perfect: #printa o final do jogo
        print('\n\nTa de hack, não errou uma meu mano!') #caso o usuário acerte todas
    elif qtd_chances >0: #caso o usuário ganhe mas erra >= 1
        print('\n\nParabéns você acertou!!!')
        print(f'Restavam {qtd_chances} chances') 
    else: #caso o usuário não acerte a palavra
        print(f'\n\nA palavra era: {palavra}\nvocê perdeu ;-;')
    menu_jogo()
jogo_forca()