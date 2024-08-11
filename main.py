my_dict = {'Alla': 2001, 'Anton': 2003, 'Karina': 2000,'Larisa': 1987}
print(my_dict)

print(my_dict.get('Alla'))
print(my_dict.get('Nikolay'))

my_dict.update({'Marina': 1983, 'Sasha': 1986})

print(my_dict.pop('Anton'))
print(my_dict)

#множество
my_set = {1, 2, 3, 3, True, 'Regina', 2, True, (1, 3, 2)}
print(my_set)
my_set.update([8, 9])
my_set.discard('Regina')
print(my_set)




