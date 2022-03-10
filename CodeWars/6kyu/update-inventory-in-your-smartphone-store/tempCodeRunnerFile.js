const objStock = {};
    for (let i = 0; i < curStock.length; i++) {
        objStock[curStock[i][1]] = curStock[i][0];
    }

    for (let i = 0; i < newStock.length; i++) {
        if (newStock[i][1] in objStock) {
            objStock[newStock[i][1]] += newStock[i][0];
        } else {
            objStock[newStock[i][1]] = newStock[i][0];
        }
    }

    const finalStock = {};
    for (let key in objStock) {
        finalStock[objStock[key]] = key;
    }
    console.log(objStock);
    // console.log(finalStock);