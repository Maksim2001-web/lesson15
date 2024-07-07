def calculate_structure_sum(data_structure):
    total_sum = 0
    total_length = 0

    def traverse_structure(element):
        nonlocal total_sum, total_length

        if isinstance(element, (list, tuple, set)):
            for item in element:
                traverse_structure(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                traverse_structure(key)
                traverse_structure(value)
        elif isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_length += len(element)

    traverse_structure(data_structure)
    return total_sum + total_length

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
