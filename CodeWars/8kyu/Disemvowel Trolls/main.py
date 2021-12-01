def disemvowel(string_):
    vogais = "aeiouAEIOU"
    no_vowels = string_
    for letra in vogais:
        no_vowels = no_vowels.replace(letra, "")
    return no_vowels


frase = "This website is for losers LOL!"
resultado_almejado = "Ths wbst s fr lsrs LL!"
print(disemvowel(frase))
print(resultado_almejado)
# The replace() method replaces a specified phrase with another specified phrase.
