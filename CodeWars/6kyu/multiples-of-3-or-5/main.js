function solution(number) {
    let num = 0;
    for (let i = 3; i < number; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            num += i;
        }
    }
    return num;
}

const teste = solution(10);
console.log(teste);
