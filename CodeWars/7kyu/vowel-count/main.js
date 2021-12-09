function getCount(str) {
    const vogais = ["a", "e", "i", "o", "u"];
    let vowelsCount = 0;

    for (let i = 0; i < vogais.length; i++) {
        for (let j = 0; j < str.length; j++) {
            if (vogais[i] === str[j]) {
                vowelsCount++;
            }
        }
    }

    console.log(vowelsCount);
    return vowelsCount;
}

getCount("valorant");

// Definition and Usage
// * The includes() method returns true if an array contains a specified element, otherwise false.
