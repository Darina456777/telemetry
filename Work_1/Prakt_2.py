#Задание 1.2

time_seconds = int(input('Введите время в секуднах: '))
hours = time_seconds // 3600
time = time_seconds % 3600
min = time // 60
sec = time % 60

print(f'Время в секундах {hours:02d}:{min:02d}:{sec:02d}')