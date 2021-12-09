function hello(name = "World") {
    let name_title = name === "" ? "World" : "";
    for (let i = 0; i < name.length; i++) {
        if (i === 0) {
            name_title += name[i].toUpperCase();
        } else {
            name_title += name[i].toLowerCase();
        }
    }

    return `Hello, ${name_title}!`;
}

console.log(hello("john"));
