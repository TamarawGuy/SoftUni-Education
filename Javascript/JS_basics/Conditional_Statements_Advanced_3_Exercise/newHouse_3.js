function newHouse(input) {
    let flower = input[0];
    let num = Number(input[1]);
    let budget = Number(input[2]);
    let result;

    if (flower == 'Roses') {
        result = num * 5;
        if (num > 80) {

            let discount = result * 0.1;
            result -= discount;
        }
    }
    else if (flower == 'Dahlias') {
        result = num * 3.8;
        if (num > 90) {
            let discount = result * 0.15;
            result -= discount;
        }
    }
    else if (flower == 'Tulips') {
        result = num * 2.8;
        if (num > 80) {
            let discount = result * 0.15;
            result -= discount;
        }
    }
    else if (flower == 'Narcissus') {
        result = num * 3;
        if (num < 120) {
            let discount = result * 0.15;
            result += discount;
        }
    }
    else if (flower == 'Gladlolus') {
        result = num * 2.5;
        if (num < 80) {
            let discount = result * 0.2;
            result -= discount;
        }
    }

    if (result > budget) {
        let money_need = (result - budget).toFixed(2);
        console.log(`Not enough money, you need ${money_need} leva more.`)
    }
    else {
        let money_left = (budget - result).toFixed(2);
        console.log(`Hey, you have a great garden with ${num} ${flower} and ${money_left} leva left.`)
    }
}