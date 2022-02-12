#Задание 1.3

n = int(input('Введите число: '))
n1 = str(n)
n2 = n1 + n1
n3 = n1 + n1 + n1
summa = n + int(n2) + int(n3)


print(f'Сложение: {n} + {n}{n} + {n}{n}{n}')
print('Сумма:', summa)