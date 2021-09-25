function ex5(arr) {
    let catalogue = {};

    arr.forEach(el => {
        let [town, product, price] = el.split(' | ');
        price = Number(price);

        if (!catalogue[product]) {
            catalogue[product] = {};
        }
        catalogue[product][town] = price;
    });

    for (const prod in catalogue) {
        const sorted = Object.entries(catalogue[prod]).sort((a, b) => a[1] - b[1]);
        console.log(`${prod} -> ${sorted[0][1]} (${sorted[0][0]})`);
    }
}


ex5(['Sofia City | Audi | 100000',
    'Sofia City | BMW | 100000',
    'Sofia City | Mitsubishi | 10000',
    'Sofia City | Mercedes | 10000',
    'Sofia City | NoOffenseToCarLovers | 0',
    'Mexico City | Audi | 1000',
    'Mexico City | BMW | 99999',
    'New York City | Mitsubishi | 10000',
    'New York City | Mitsubishi | 1000',
    'Mexico City | Audi | 100000',
    'Washington City | Mercedes | 1000'
])

// Output:
// Audi -> 100000 (Sofia City)
// BMW -> 99999 (Mexico City)
// Mitsubishi -> 1000 (New York City)
// Mercedes -> 1000 (Washington City)
// NoOffenseToCarLovers -> 0 (Sofia City)