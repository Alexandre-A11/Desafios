def update_inventory(cur_stock, new_stock):
    dict_stock = {brand[1]: brand[0] for brand in cur_stock}

    for brand in new_stock:
        if brand[1] in dict_stock:
            dict_stock[brand[1]] += brand[0]
        else:
            dict_stock[brand[1]] = brand[0]

    reversed_dict = [(value, key) for (key, value) in sorted(dict_stock.items())]
    return reversed_dict


# Testes:
cur_stock = [(25, "HTC"), (1000, "Nokia"), (50, "Samsung"), (33, "Sony"), (10, "Apple")]
new_stock = [(5, "LG"), (10, "Sony"), (4, "Samsung"), (5, "Apple")]

print(update_inventory(cur_stock, new_stock))
