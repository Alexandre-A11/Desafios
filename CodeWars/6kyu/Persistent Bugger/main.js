// My Method 1~ 🦉
// prettier-ignore
function persistence(num) {
    let arrayNum = num;
    let count = 0;
    while (String(arrayNum).length > 1) {
        let multiply = 1;
        String(arrayNum).split("").map(function (element) {
                multiply *= element;
            });
            arrayNum = multiply;
            count++;
            console.log(arrayNum);
    }
    return count;
}

// Method 2: 🐉
function persistence_2(num) {
    let qtd = 0;
    numString = num.toString();
    while (numString.length > 1) {
        qtd++;
        numString = numString
            .split("")
            .map(Number)
            .reduce((prev, curr) => prev * curr)
            .toString();
    }
    return qtd;
}

const test_case = 999;
console.log(persistence_2(test_case));
