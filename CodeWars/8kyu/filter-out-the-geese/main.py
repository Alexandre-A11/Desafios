geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    # your code here
    new_list = [string for string in birds if string not in geese]
    return new_list


lista_teste = ["Mallard", "Hook Bill", "African",
               "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
goose_filter(lista_teste)
