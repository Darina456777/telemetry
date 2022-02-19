




my_voc = {1: 'value', ' printer' : 3, 'price' : 400}
my_voc2 = {5: 100, 'pruppa': 12}
my_voc["xerox"] = 55

print(my_voc)
print(my_voc.get('printer'))




massive = [1,2,3,4]

my_set={1,3,5,6,8}
my_set_2 = set(massive)

my_set3 = my_set - my_set_2

print(my_set)
print(hash("my_set_2"))
print(my_set3)





massive.append(1000)
my_turple= tuple(massive)

print(my_turple)











massive = [1, 2, 3, 4, 5, 'today', False]
massive2 = [1,2,3,4]
massive3 = massive2
massive2.append(50)

massive3.append(100)

print(massive2[:: -1])
print(massive3)


print(len(massive))

massive.append(7)

print(massive[5])
print(len(massive))

massive[2]=5

print(massive)

massive.insert(2,10)
print(massive)