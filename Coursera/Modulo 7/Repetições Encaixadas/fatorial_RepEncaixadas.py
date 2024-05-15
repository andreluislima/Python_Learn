

num = int(input('Digite um número inteiro maior que 0: '))
fat = 1
while True:
    if num == 0:
        print('FIM')
        break
    while num > 0:
        print(num)
        fat = fat * num
        num = num - 1
print(fat)

