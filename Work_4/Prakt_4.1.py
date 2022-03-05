#Задание 4.1

myfile = open('myfile.txt', 'w')
line = input('Введите текст \n')
while line:
    myfile.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

myfile.close()
