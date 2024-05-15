
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
c = altura

while c > 0:
    print(altura * '', end='')
    c-=1
    while altura > 0:
        if largura == 2:
            print(largura * '#')
            altura -=1
        else:
            while True:
                if altura % 2 == 1:
                    print(largura * '#')
                    altura -=1
                else:
                    n = largura - (largura - 1)
                    espaco = largura - 2
                    print((n * '#') + (espaco * ' ') + (n * '#'))
                    altura -= 1
                if altura == 0:
                    break
