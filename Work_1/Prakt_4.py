#Задание 1.4

number = int(input('Введите число:'))
number_max = number % 10
number = number // 10
while number > 0:
    if number % 10 > number_max :
        number_max = number % 10
    number = number // 10

print('Самая большая цифра в числе: ', number_max)