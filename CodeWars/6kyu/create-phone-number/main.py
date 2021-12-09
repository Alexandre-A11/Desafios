def create_phone_number(n):
    # your code here
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")

    converter_em_string = "".join(str(numero) for numero in n)
    return converter_em_string
