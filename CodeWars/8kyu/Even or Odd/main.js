function even_or_odd(number) {
    return number % 2 === 0 ? "Even" : "Odd";
    // return !(number % 2) ? "Even" : "Odd";
    // return number % 2 ? "Odd" : "Even";
}

test_case = even_or_odd(11);
console.log(test_case);
