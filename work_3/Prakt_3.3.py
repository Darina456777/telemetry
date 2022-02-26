# Задание 3.3

def my_func(number1, number2, number3):
    print(f'Сумма двух наибольших аргументов: {number1 + number2 + number3 - min([number1, number2, number3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)