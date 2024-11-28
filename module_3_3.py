def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)
print_params(b = 31)
print_params(c = [4, 5, 6])
values_list = ['Евгений', 777, [4, 5, 6]]
values_dict = {'a': [4, 5, 6], 'b': 'Евгений', 'c': 777}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['абв', [1, 2, 3]]
print_params(*values_list_2, 42)