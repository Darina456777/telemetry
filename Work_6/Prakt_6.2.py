#Задание 2
import sys

inp1 = input('Введите первое значение: ')
inp2 = input('Введите второе значение: ')

try:

    int(inp1)
    int(inp2)
except ValueError:
    print(f'{inp1} или {inp2} Переменная должна быть числом')
    sys.exit()
except TypeError:
    print(f'{inp1} или {inp2} Переменная должна быть числом')
    sys.exit()


def ss(inp1, inp2):
    x1 = int(inp1)
    x2 = int(inp2)
    try:
        if x1 < x2:
            for x in range(x1, x2+1):
                print(x)
                x = x + 1
        elif x2 < x1:
            for x in reversed(range(x2, x1+1)):
                print(x)
                x = x - 1;


    except ValueError:
        print(f'{x1} или {x2} Неверные значение')

    except FloatingPointError:
        print (f'{x1} или {x2} Число должно быть целым')


ss(inp1, inp2)

