// My Method 1~ 🦉
function digital_root(n) {
    const sum_numbers = (number_string) => {
        let sum = 0;
        for (let i = 0; i < number_string.length; i++) {
            sum += Number(number_string[i]);
        }
        return sum;
    };

    result = sum_numbers(String(n));

    while (result > 9) {
        result = sum_numbers(String(result));
    }

    return result;
}

const test_case = digital_root(493193);
console.log(test_case);
