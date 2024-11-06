# Работа со словарями
my_dict = {'Den': 1981, 'Max': 1982, 'Alex': 1983}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Ann', 'Такое значение отсутствует'))
my_dict.update({'Flo': 1984, 'Wer': 1985})
print(my_dict)
new_dict = my_dict.pop('Den')
print(new_dict)
print(my_dict)

# Работа с множествами
my_set = {2, 3, 4, 1, 3, 5, 4, 'Fet', 'Den', 'Fet', (2, 1, 3)}
print(my_set)
my_set.update({6, 7})
my_set.remove((2, 1, 3))
print(my_set)