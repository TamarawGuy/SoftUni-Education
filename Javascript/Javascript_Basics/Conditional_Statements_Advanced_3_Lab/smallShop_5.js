function shop(input) {
    let product = input[0];
    let town = input[1];
    let quantity = Number(input[2]);
    let result;

    if (town == 'Sofia') {
        if (product == 'coffee') {
            result = 0.5 * quantity;
        }
        else if (product == 'water') {
            result = 0.8 * quantity;
        }
        else if (product == 'beer') {
            result = 1.2 * quantity;
        }
        else if (product == 'sweets') {
            result = 1.45 * quantity;
        }
        else if (product == 'peanuts') {
            result = 1.6 * quantity;
        }
    }
    else if (town == 'Plovdiv') {
        if (product == 'coffee') {
            result = 0.4 * quantity;
        }
        else if (product == 'water') {
            result = 0.7 * quantity;
        }
        else if (product == 'beer') {
            result = 1.15 * quantity;
        }
        else if (product == 'sweets') {
            result = 1.3 * quantity;
        }
        else if (product == 'peanuts') {
            result = 1.5 * quantity;
        }
    }
    else if (town == 'Varna') {
        if (product == 'coffee') {
            result = 0.45 * quantity;
        }
        else if (product == 'water') {
            result = 0.7 * quantity;
        }
        else if (product == 'beer') {
            result = 1.1 * quantity;
        }
        else if (product == 'sweets') {
            result = 1.35 * quantity;
        }
        else if (product == 'peanuts') {
            result = 1.55 * quantity;
        }
    }
    console.log(result);
}