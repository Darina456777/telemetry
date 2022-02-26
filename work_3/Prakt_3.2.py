# Задание 3.2

def anketa(name, lastname, year_of_birth, city_of_residence, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth} Город проживания: {city_of_residence} Email: {email} Телефон: {phone}')

anketa(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city_of_residence=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)