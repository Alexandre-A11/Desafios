function updateInventory(curStock, newStock) {
    const objStock = {};
    // Converter Array para Objeto:
    for (let i = 0; i < curStock.length; i++) {
        objStock[curStock[i][1]] = curStock[i][0];
    }

    // Soma valor em Key já existente, ou cria Key com Valor.
    for (let i = 0; i < newStock.length; i++) {
        if (newStock[i][1] in objStock) {
            objStock[newStock[i][1]] += newStock[i][0];
        } else {
            objStock[newStock[i][1]] = newStock[i][0];
        }
    }

    // Ordenar em Ordem Alfabética
    arrayStock = Object.entries(objStock).sort((a, b) =>
        a[0].localeCompare(b[0])
    );

    // Inverter Posições de [Marca, Quantidade] para [Quantidade, Marca]
    for (i = 0; i < arrayStock.length; i++) {
        arrayStock[i].splice(0, 2, arrayStock[i][1], arrayStock[i][0]);
    }
    return arrayStock;
}

// ! Solucação Interessante:
/*
function updateInventory(curStock, newStock) {
    let obj = {};
    curStock.concat(newStock).forEach(([cnt, name]) => {
        obj[name] ? (obj[name] += cnt) : (obj[name] = cnt);
    });
    return Object.keys(obj)
        .sort()
        .map((k) => [obj[k], k]);
}
*/

// Testes:
curStock = [
    [25, "HTC"],
    [1000, "Nokia"],
    [50, "Samsung"],
    [33, "Sony"],
    [10, "Apple E"],
];
newStock = [
    [5, "LG"],
    [10, "Sony"],
    [4, "Samsung"],
    [5, "Apple"],
];

console.log(updateInventory(curStock, newStock));
