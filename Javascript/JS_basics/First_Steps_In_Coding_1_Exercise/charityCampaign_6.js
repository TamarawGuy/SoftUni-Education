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