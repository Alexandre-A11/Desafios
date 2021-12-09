def hello(name="World"):
    name = "World" if name == "" else name
    return f"Hello, {name.title()}!"


print(hello())
