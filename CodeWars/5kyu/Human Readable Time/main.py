def make_readable(seconds):
    ss = seconds % 60
    mm = seconds // 60
    hh = seconds // 60 // 60

    if mm > 59:
        mm = mm % 60

    if ss < 10:
        ss = f"0{ss}"
    if mm < 10:
        mm = f"0{mm}"
    if hh < 10:
        hh = f"0{hh}"
    return f"{hh}:{mm}:{ss}"


# Teste
print(make_readable(9595))
