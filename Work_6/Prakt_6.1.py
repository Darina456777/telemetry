def wert(number_1, number_2):
   result = 0
   try:
      result = number_1 + number_2
   except TypeError as error:
       result = f'{number_1} or {number_2} Переменные числа'
   finally:
       print('программа завершилась, до свидания')

   return result

print(wert(5, 9))
