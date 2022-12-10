const romanToInt = function (s) {
    const roman = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };

    const except = {
        IV: 4,
        IX: 9,
        XL: 40,
        XC: 90,
        CD: 400,
        CM: 900,
    };

    let sum = 0;
    const regex = s.match(/IV|IX|XL|XC|CD|CM/g);

    if (regex) {
        regex.map(e => {
            sum += except[e];
            s = s.replace(e, "");
        });
    };
    
    s.split("").map((e) => {
        sum += roman[e];
    });

    return sum;
};

console.log(romanToInt("I"));
console.log(romanToInt("XIV"));
console.log(romanToInt("MCMXCIV"));