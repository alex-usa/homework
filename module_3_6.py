data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    all_length = 0
    for i in data_structure:
        if isinstance(i, int):
            all_length += i
        elif isinstance(i, str):
            all_length += len(i)
        elif isinstance(i, (list, tuple, set)):
            all_length += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                all_length += calculate_structure_sum([key])
                all_length += calculate_structure_sum([value])
    return all_length

result = calculate_structure_sum(data_structure)
print(result)
