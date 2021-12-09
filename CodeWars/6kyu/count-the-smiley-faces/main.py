def count_smileys(arr):
    cont = 0
    for faces in arr:
        if ":" in faces or ";" in faces:
            if len(faces) != 2:
                if "-" in faces or "~" in faces:
                    if ")" in faces or "D" in faces:
                        cont += 1
            else:
                if ")" in faces or "D" in faces:
                    cont += 1

    return cont
