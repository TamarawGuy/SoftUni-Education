function shop(input) {
    let product = input[0];
    let day = input[1];
    let quantity = Number(input[2]);
    let result = 0;

    if (day == 'Saturday' || day == 'Sunday') {
        if (product == 'banana') {
            result = quantity * 2.7;
        }
        else if (product == 'apple') {
            result = 1.25 * quantity;
        }
        else if (product == 'orange') {
            result = quantity * 0.9;
        }
        else if (product == 'grapefruit') {
            result = quantity * 1.6;
        }
        else if (product == 'kiwi') {
            result = 3 * quantity;
        }
        else if (product == 'pineapple') {
            result = quantity * 5.6;
        }
        else if (product == 'grapes') {
            result = quantity * 4.2;
        }
        else {
            console.log('error');
        }
    }
    else if (day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' || day == 'Friday') {
        if (product == 'banana') {
            result = quantity * 2.5;
        }
        else if (product == 'apple') {
            result = 1.2 * quantity;
        }
        else if (product == 'orange') {
            result = quantity * 0.85;
        }
        else if (product == 'grapefruit') {
            result = quantity * 1.45;
        }
        else if (product == 'kiwi') {
            result = 2.7 * quantity;
        }
        else if (product == 'pineapple') {
            result = quantity * 5.5;
        }
        else if (product == 'grapes') {
            result = quantity * 3.85;
        }
        else {
            console.log('error');
        }
    }
    else {
        console.log('error');
    }

    if (result != 0) {
        result = (result).toFixed(2);
        console.log(result);
    }
}