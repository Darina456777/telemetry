# Задание 3.6

def int_func(text):
    return text.title()
stroka = []


for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    stroka.append(int_func(word))

print(f'Вариант1 Строка получается вот такая: {" ".join(stroka)}')
