// 🦉 My Method:
// prettier-ignore
function duplicateEncode(word) {
    Array.prototype.count = function (element) {
        let count = 0;
        this.forEach((item) => {
            if (item === element) {
                count++;
            }
        });

        return count;
    };
    const wordArray = Array.from(word.toLowerCase());

    return Array.from(word.toLowerCase()).map((element) => {
            return wordArray.count(element) > 1 ? ")" : "(";
        }).join("");
}

const test_case = ["din", "recede", "Success", "(( @"];
test_case.forEach((element, index) => console.log(duplicateEncode(element)));
