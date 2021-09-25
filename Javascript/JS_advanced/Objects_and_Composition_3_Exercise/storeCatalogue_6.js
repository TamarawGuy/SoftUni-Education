function storaCatalogue(arr) {
    let objects = [];

    for (const item of arr) {
        let [name, price] = item.split(' : ');
        price = Number(price);

        let obj = {
            name,
            price
        }

        objects.push(obj);
    }

    objects.sort((a, b) => a.name.localeCompare(b.name));

    let letter = objects[0].name.charAt(0);
    console.log(letter);

    for (const obj of objects) {
        let firstLetter = obj.name.charAt(0);
        if (firstLetter === letter) {
            console.log(`  ${obj.name}: ${obj.price}`);
        }
        else {
            letter = obj.name.charAt(0);
            console.log(letter);
            console.log(`  ${obj.name}: ${obj.price}`);
        }
    }
}