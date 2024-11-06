immutable_var = 1, 2, 'peach'
print(immutable_var)

# пытаться изменить кортеж не буду, он неизменный. Но к нему можно прибавлять и его можно умножать. Но внутри него нельзя менять данные

mutable_list = [1, 2, 'peach']
mutable_list[0] = 3
print(mutable_list)