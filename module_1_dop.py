grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# считаем среднее
average = [sum(grade) / len(grade) for grade in grades]

# преобразуем множества в список и сортируем
my_list = list(students)
my_list.sort()

# составляем словарь студент-балл
dictionary = dict(zip(my_list, average))
print(dictionary)