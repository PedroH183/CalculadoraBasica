def tracinho():
    print ('_'*30)

# Parte responsável por puxar as operações com os valores inseridos na princial()
def operacoes(X,Y, U):
    while True:
        if U == '01':
            W = (X + Y)
            print ('O resultado de sua soma é '+ str(W) +'\n ')
            break
        if U == '02':
            W = (X - Y)
            print ('O resultado de sua subtração é '+ str(W)+ '\n')
            break
        if U == '03':
            W = (X / Y)
            print ('O resultado de sua divisão é '+ str(W)+ '\n ')
            break
        if U == '04':
            W = (X * Y)
            print ('O resultado de sua multiplicação é '+str(W)+ '\n')
            break
        if U != ('01' or '02' or '03' or '04'):
            print ('\nVocê esta inserindo valores errados !!! \n insira valores válidos\n !!')
            lista()
            U = str(input('\n Escolha uma operação (digite o valor referente)\n'))
        continue
    
# Parte responsável por inserir o cabeçalho principal da calculadora
def cabeçalho(txt):
    tracinho()
    print (txt)
    tracinho()

# Parte responsável por exibir uma lista para a seleção da operação desejada ! 
def lista():
    lis = ['soma-01','subtração-02','divisão-03','Multiplicação-04']
    for z in lis:
        print(z)

    tracinho()

# Parte responsável por realizar a releitura ao final do progama, caso desejado// 
# Evita que a calculadora encerre ao realizar apenas uma operação, então a reinicia
def ultima():
    V = str(input('Deseja rodar a calcuculadora novamente ?? \n Responda sim ou não\n'))
    if V == ('sim'):
        principal()
    if V == ('não'):
        exit()

# Código principal onde se insere os dois valores 
def principal():
    cabeçalho('Calculadora Básica')
    X = float(input ('Escreva o primeiro valor\n'))
    print()
    tracinho()
    Y = float(input('Escreva o segundo valor\n'))
    print()
    cabeçalho('Aqui estão as operações possíveis no momento !!\n')
    lista()
    U = str(input('\n Escolha uma operação (digite o valor referente)\n'))
    
    operacoes(X, Y, U)
    ultima()



principal()