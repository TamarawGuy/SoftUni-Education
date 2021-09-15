function fromUSDToBGN(input) {
    let num = Number(input[0]);
    let bgn = num * 1.79549;
    console.log(bgn);
}

function fromRadiansToDegrees(input) {
    let radians = Number(input[0])
    let degrees = (radians * 180 / Math.PI).toFixed(0);
    console.log(degrees);
}

function calculateDeposits(input) {
    let deposit = Number(input[0])
    let months = Number(input[1])
    let apy = Number(input[2])

    let interest = deposit * apy / 100;
    let interestOneMonth = interest / 12;
    let total = deposit + (months * interestOneMonth);
    console.log(total);
}

function bookList(input) {
    let pages = Number(input[0]);
    let pages1Hour = Number(input[1]);
    let days = Number(input[2]);

    let totalHours = pages / pages1Hour;
    let hoursPerDay = totalHours / days;
    console.log(hoursPerDay);
}

function birthday(input) {
    let rent = Number(input[0]);
    let cake = rent * 20 / 100;
    let drinks = cake - (cake * 45 / 100);
    let animator = rent / 3;
    let total = rent + cake + drinks + animator;
    console.log(total);
}

function charity(input) {
    let days = Number(input[0]);
    let sladkar = Number(input[1]);
    let cakes = Number(input[2]);
    let waffles = Number(input[3]);
    let pancakes = Number(input[4]);

    let price_cakes = cakes * 45;
    let price_waffles = waffles * 5.8;
    let price_pancakes = pancakes * 3.2;
    let price_1_day = (price_cakes + price_waffles + price_pancakes) * sladkar;
    let total = price_1_day * days;
    let total_after_payment = total - (total * 1 / 8);
    console.log(total_after_payment);
}

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

function aquarium(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let p = Number(input[3]);

    let volume = length * width * height;
    let liters = volume * 0.001;
    let percent = p * 0.01;
    let total = liters * (1 - percent);
    console.log(total);
}