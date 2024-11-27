from random import randint
first_stone = randint(3, 20)

first_number = 1
second_number = first_number
if first_stone % 2 != 0:
    max_number = first_stone // 2 + 1
else:
    max_number = first_stone // 2

pair = []

for i in range(max_number):
    # pair_n = []
    for j in range(first_stone - 1):
        if first_stone % (first_number + second_number) == 0:
            pair.append(f'{first_number}{second_number}')
        second_number += 1
        # pair.append(pair_n)
    first_number += 1
    second_number = first_number

print(f"{'result:'} {first_stone} {'-'} {''.join(pair)}")
