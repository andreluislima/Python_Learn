
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
c = altura

while c > 0:
    print(altura * '', end='')
    c-=1
    while altura > 0:
        print(largura * '#')
        altura -=1