function fruit(type, grams, price) {
    console.log(`I need $${(grams * price / 1000).toFixed(2)} to buy ${(grams / 1000).toFixed(2)} kilograms ${type}.`);
}