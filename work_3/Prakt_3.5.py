# Задание 3.5

def numbers(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = numbers(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_flag:
        break
