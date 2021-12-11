function cleverLilly(input) {
    let age = Number(input[0]);
    let washing_machine = Number(input[1]);
    let toy_price = Number(input[2]);

    let toys = 0;
    let money = 0;
    let lilly_money = 0;
    let counter = 0

    for (let i = 1; i < age + 1; i++) {
        if (i % 2 == 0) {
            money += 10;
            lilly_money += money;
            counter += 1;
        }
        else {
            toys += 1;
        }
    }

    let total_price_toys = toys * toy_price;
    let total = total_price_toys + lilly_money;
    total -= counter;

    if (total >= washing_machine) {
        let money_left = (total - washing_machine).toFixed(2);
        console.log(`Yes! ${money_left}`);
    }
    else {
        let money_needed = (washing_machine - total).toFixed(2);
        console.log(`No! ${money_needed}`);
    }
}