// My Method 1~ 🙃
function likes(names) {
    const message = [
        `no one likes`,
        `${[names[0]]} likes`,
        `${[names[0]]} and ${[names[1]]} like`,
        `${[names[0]]}, ${[names[1]]} and ${[names[2]]} like`,
        `${[names[0]]}, ${[names[1]]} and ${[names.length - 2]} others like`,
    ];
    const index = names.length > 4 ? 4 : names.length;
    return `${message[index]} this`;
}

const namesArray = ["Alex", "Jacob", "Mark", "Max"];
const test_case = likes(namesArray);
console.log(test_case);
