function buildString(...template) {
    return `I like ${template.join(", ")}!`;
}

const test = buildString("Cheese", "Milk", "Chocolate");
console.log(test);
