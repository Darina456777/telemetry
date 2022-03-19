
import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def devizion(a, b, c):

  try:
     D = b ** 2 - 4 * a * c
     x1 = (-b + math.sqrt(D)) / 2 * a
     x2 = (-b - math.sqrt(D)) / 2 * a

     print("Дискриминант D = %.2f" % D)

  except TypeError:
    D = f'{a},{b},{c} Переменная должна быть числом'
  except UnboundLocalError:
     x1 = 'Корня нет'
     x2= 'Корня нет'
  except ValueError:
     x1 = 'Корня нет'
     x2 = 'Корня нет'

  return D, x1, x2



#График
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)
y = a * x ** 2 + b * x - c

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
