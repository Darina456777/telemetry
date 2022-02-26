# Задание 3.1

def numbers(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Делить на ноль нельзя')

print(numbers(int(input('число 1: ')), int(input('число 2: '))))
