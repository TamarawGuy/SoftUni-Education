function cinema(input) {
    let budget = Number(input[0]);
    let statists = Number(input[1]);
    let price_1_outfit = Number(input[2]);

    let price_decor = budget * 0.1;
    let price_outfit = price_1_outfit * statists;
    if (statists > 150) {
        price_outfit -= price_outfit * 0.1;
    }

    let total = price_decor + price_outfit;

    if (total > budget) {
        money_needed = (total - budget).toFixed(2);
        console.log("Not enough money!");
        console.log(`Wingard needs ${money_needed} leva more.`)
    }
    else {
        money_left = (budget - total).toFixed(2);
        console.log("Action!");
        console.log(`Wingard starts filming with ${money_left} leva left.`)
    }
}