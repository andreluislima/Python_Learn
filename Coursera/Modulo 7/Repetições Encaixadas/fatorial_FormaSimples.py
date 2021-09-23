
n = 8 # variavel que receberá o numero do fatorial
c = n # contador para auxilio do cálculo.
# Será esse contador que receberá a cada iteração um valor que será multiplicado
# pelo numero.
fat = 1 # valor minimo do

while c > 0:
    print(c)
    fat = fat * c
    c = c - 1

print(fat)