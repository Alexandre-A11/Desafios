// My Method 1~ 🦉
// prettier-ignore
function duplicateCount(text) {
    let count = 0;
    const lowerText = text.toLowerCase();
    const oldArray = [];
    for (let i = 0; i < text.length; i++) {
        if (lowerText.slice(i + 1).includes(lowerText[i]) && !oldArray.includes(lowerText[i])) {
            count++;
            oldArray.push(lowerText[i]);
        }
    }
    return count;
}
// My Method 2~ 🐬
// prettier-ignore
function duplicateCount_2(text) {
    const lowerText = text.toLowerCase().split("");
    const usedArray = [];
    let count = 0;
    lowerText.map(function (element, i) {
        if (lowerText.slice(i + 1).includes(element) && !usedArray.includes(element)) {
            count++;
            usedArray.push(element);
        }
    });
    return count;
}

const testsArray = [
    "abcde",
    "aabbcde",
    "aabBcde",
    "indivisibility",
    "Indivisibilities",
    "aA11",
    "ABBA",
];

for (let i = 0; i < testsArray.length; i++) {
    console.log(duplicateCount_2(testsArray[i]));
}
