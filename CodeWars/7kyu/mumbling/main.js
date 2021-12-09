// My Method 1~ 🦉
function accum(s) {
    const array = s.split("");
    const new_array = [];
    for (let i = 0; i < array.length; i++) {
        new_array.push(
            array[i].toUpperCase() + array[i].repeat(i).toLowerCase()
        );
    }
    return new_array.join("-");
}

const test_case = accum("RqaEzty");
console.log(test_case);
