//  Find the odd int

// My Method 1~ 🦉
function findOdd(A) {
    const number_of_times = [];
    const numbers = [];
    for (let i = 0; i < A.length; i++) {
        let count = 0;
        for (let j = 0; j < A.length; j++) {
            if (A[i] === A[j]) {
                count++;
            }
        }
        if (!number_of_times.includes(count)) {
            number_of_times.push(count);
            numbers.push(A[i]);
        }
    }
    // console.log(number_of_times);
    // console.log(numbers);

    let odd;
    for (let i = 0; i < number_of_times.length; i++) {
        if (number_of_times[i] % 2) {
            // console.log(numbers[i]);
            odd = numbers[i];
        }
    }

    return odd;
}

// My Method 2~ 🐼
function findOdd_2(A) {
    const numbers = [];
    for (let i = 0; i < A.length; i++) {
        !numbers.includes(A[i]) ? numbers.push(A[i]) : null;
    }

    let odd = null;
    for (let i = 0; i < numbers.length; i++) {
        let count = 0;
        for (let j = 0; j < A.length; j++) {
            numbers[i] === A[j] ? count++ : null;
        }
        // console.log(count);
        if (odd === null) {
            odd = count % 2 !== 0 ? numbers[i] : null;
        }
        // console.log(`Odd: ${odd}`);
    }
    // console.log(numbers);
    return odd;
}

const test_case = findOdd_2([1, 1, 2]);
console.log(test_case);
