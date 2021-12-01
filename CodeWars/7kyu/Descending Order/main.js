// My Method 1~ 🦉
function descendingOrder(n) {
    // return Number(n.toString().split("").sort().reverse().join(""));
    return Number(Array.from(n.toString()).sort().reverse().join(""));
}

const tests_cases = [42145, 145263, 123456789];
tests_cases.forEach((element) => console.log(descendingOrder(element)));

// TODO
//  intenger > string
//  converter elementos para number
//  usar sort method
//  converter para string novamente
//  concatenar
//  number
