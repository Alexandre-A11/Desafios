function disemvowel(str) {
    no_vowels = str.replace(/a|e|i|o|u/gi, "");
    return no_vowels;
}

const frase_teste = "This website is for losers LOL!";
const frase_resultado = "Ths wbst s fr lsrs LL!";

console.log(disemvowel(frase_teste));
console.log(frase_resultado);

// The replace() method searches a string for a specified value, or a regular expression, and returns a new string where the specified values are replaced.
// string.replace(searchvalue, newvalue)
// g = Perform a global replacement:
// gi = Perform a global, case-insensitive replacement:
