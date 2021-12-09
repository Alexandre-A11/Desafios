// My Method 1~ 🦉
function spinWords(string) {
    const strArray = string.split(" ");

    for (let i = 0; i < strArray.length; i++) {
        if (strArray[i].length >= 5) {
            strArray[i] = strArray[i].split("").reverse().join("");
        }
    }
    return strArray.join(" ");
}

const test_case = spinWords("Hey fellow warriors");
console.log(test_case);
