function fruitMarket(input) {
    let price_strawberries = Number(input[0]);
    let bananas = Number(input[1]);
    let oranges = Number(input[2]);
    let raspberries = Number(input[3]);
    let strawberries = Number(input[4]);

    let price_raspberries = price_strawberries / 2;
    let price_oranges = price_raspberries - (price_raspberries * 0.4);
    let price_bananas = price_raspberries - (price_raspberries * 0.8);

    let total_raspberries = price_raspberries * raspberries;
    let total_oranges = price_oranges * oranges;
    let total_bananas = price_bananas * bananas;
    let total_strawberries = price_strawberries * strawberries;

    let total = total_raspberries + total_oranges + total_bananas + total_strawberries;
    console.log(total);
}