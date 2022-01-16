def dna_to_rna(dna):
    return "".join(["U" if letter == "T" else letter for letter in dna])


print(dna_to_rna("GCAT"))
