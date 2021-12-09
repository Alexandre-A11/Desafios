// My Method 1~ 🦉
function squareDigits(num) {
    const str = String(num);
    let new_str = "";
    for (let i = 0; i < str.length; i++) {
        new_str += String(Number(str[i]) ** 2);
    }
    return Number(new_str);
}

test_case = squareDigits(9119);
console.log(test_case);
