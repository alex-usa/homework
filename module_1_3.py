name = 'Alex'
print('Name: ' + name)
age = 43
print('Age: ' + str(age))
new_age = age + 1
print('New age: ' + str(new_age))
is_student = True
print('Is Student: ' + str(is_student))

numbers_of_dz = 12
number_of_hours = 1.5
name_of_kurs = 'Python'
time_to_1_dz = number_of_hours / numbers_of_dz
print('Курс: ' + str(name_of_kurs) + ',' + ' всего задач: ' + str(numbers_of_dz) + ',' + ' затрачено часов: ' + str(number_of_hours) + ',' + ' среднее время выполнения ' + str(time_to_1_dz) + ' часа.')
print('Курс: ', name_of_kurs, ', всего задач: ', numbers_of_dz, ', затрачено часов: ', number_of_hours, ', среднее время выполнения ', time_to_1_dz, ' часа.', sep='')

example = 'MacBookPro16'
print(example[0])
print(example[-1])
print(example[7:12])
print(example[::-1])
print(example[1::2])

name = input('Введите ваше имя: ')
print(type(name))