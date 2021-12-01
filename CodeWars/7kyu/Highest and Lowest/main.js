// My Method 1~ 🦉
function highAndLow(numbers) {
    const number_list = numbers.split(" ").map(function (num) {
        return Number(num);
    });

    console.log(number_list);

    const max_and_min = function (operation) {
        return number_list.reduce(function (prevVal, currVal) {
            return operation === "max"
                ? Math.max(prevVal, currVal)
                : Math.min(prevVal, currVal);
        });
    };

    // prettier-ignore
    const max = max_and_min("max"), min = max_and_min("min");

    return `${max} ${min}`;
}

// Method 2:
function highAndLow_2(numbers) {
    const numberArray = numbers.split(" ");
    console.log(...numberArray);
    return `${Math.max(...numberArray)} ${Math.min(...numberArray)}`;
}

const test_case = highAndLow_2("1 2 3 4 5");
console.log(test_case);

// Tests Reduce and Split
const split = "1 2 3 4 5".split(" ").map(function (num) {
    return Number(num);
});

const reduce = split.reduce(function (a, b) {
    return Math.max(a, b);
});
