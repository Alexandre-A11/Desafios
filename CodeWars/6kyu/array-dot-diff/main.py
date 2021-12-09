def array_diff(a, b):
    new_list = a
    for i in b:
        while i in a:
            new_list.remove(i)
    return new_list
