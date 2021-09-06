function dayOfTheWeek(input) {
    let num = Number(input[0]);

    if (num == 1) {
        console.log('Monday')
    }
    else if (num == 2) {
        console.log('Tuesday')
    }
    else if (num == 3) {
        console.log('Wednesday')
    }
    else if (num == 4) {
        console.log('Thursday')
    }
    else if (num == 5) {
        console.log('Friday')
    }
    else if (num == 6) {
        console.log('Saturday')
    }
    else if (num == 7) {
        console.log('Sunday')
    }
    else {
        console.log('Error')
    }
}

function workOrDayOff(input) {
    let day = input[0];

    if (day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' || day == 'Friday') {
        console.log('Working day');
    }
    else if (day == 'Saturday' || day == 'Sunday') {
        console.log('Weekend');
    }
    else {
        console.log("Error")
    }
}

function animalType(input) {
    let animal = input[0];

    if (animal == 'dog') {
        console.log('mammal');
    }
    else if (animal == 'crocodile' || animal == 'tortoise' || animal == 'snake') {
        console.log('reptile');
    }
    else {
        console.log('unknown');
    }
}

function greet(input) {
    let age = Number(input[0]);
    let sex = input[1];

    if (sex == 'm') {
        if (age >= 16) {
            console.log('Mr.')
        }
        else {
            console.log('Master')
        }
    }
    else {
        if (age >= 16) {
            console.log('Ms.')
        }
        else {
            console.log('Miss')
        }
    }
}

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

function numInInterval(input) {
    let num = Number(input[0]);
    let result = 'No';

    if (num != 0) {
        if (num >= -100 && num <= 100) {
            result = 'Yes';
            console.log(result);
        }
        else {
            console.log(result);
        }
    }
    else {
        console.log(result);
    }
}

function workingTime(input) {
    let hour = Number(input[0]);
    let day = input[1];

    if (day == 'Sunday') {
        console.log('closed');
    }
    else {
        if (hour >= 10 && hour <= 18) {
            console.log('open');
        }
        else {
            console.log('closed');
        }
    }
}

function cinemaTicket(input) {
    let day = input[0];

    if (day == 'Saturday' || day == 'Sunday') {
        console.log(16);
    }
    else if (day == 'Wednesday' || day == 'Thursday') {
        console.log(14);
    }
    else {
        console.log(12);
    }
}

function fruitOrVegetable(input) {
    let product = input[0];

    if (product == 'banana' || product == 'apple' || product == 'kiwi' || product == 'cherry' || product == 'lemon' || product == 'grapes') {
        console.log('fruit');
    }
    else if (product == 'tomato' || product == 'cucumber' || product == 'pepper' || product == 'carrot') {
        console.log('vegetable');
    }
    else {
        console.log('unknown');
    }
}

function invalidNumber(input) {
    let num = Number(input[0]);

    if ((num < 100 || num > 200) && num != 0) {
        console.log('invalid');
    }
}

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

function trade(input) {
    let town = input[0];
    let sales = Number(input[1]);
    let result = 0;

    if (town == 'Sofia') {
        if (sales >= 0 && sales <= 500) {
            result = sales * 0.05;
        }
        else if (sales > 500 && sales <= 1000) {
            result = sales * 0.07;
        }
        else if (sales > 1000 && sales <= 10000) {
            result = sales * 0.08;
        }
        else if (sales > 10000) {
            result = sales * 0.12;
        }
        else {
            console.log('error')
        }

    }
    else if (town == 'Varna') {
        if (sales >= 0 && sales <= 500) {
            result = sales * 0.045;
        }
        else if (sales > 500 && sales <= 1000) {
            result = sales * 0.075;
        }
        else if (sales > 1000 && sales <= 10000) {
            result = sales * 0.1;
        }
        else if (sales > 10000) {
            result = sales * 0.13;
        }
        else {
            console.log('error')
        }
    }
    else if (town == 'Plovdiv') {
        if (sales >= 0 && sales <= 500) {
            result = sales * 0.055;
        }
        else if (sales > 500 && sales <= 1000) {
            result = sales * 0.08;
        }
        else if (sales > 1000 && sales <= 10000) {
            result = sales * 0.12;
        }
        else if (sales > 10000) {
            result = sales * 0.145;
        }
        else {
            console.log('error')
        }
    }
    else {
        console.log('error')
    }

    if (result != 0) {
        result = (result).toFixed(2);
        console.log(result);
    }
}

function holiday(input) {
    let nights = Number(input[0]) - 1;
    let type_room = input[1];
    let grade = input[2];
    let result;
    let discount;

    if (type_room == 'room for one person') {
        result = nights * 18;

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    else if (type_room == 'apartment') {
        if (nights < 10) {
            result = nights * 25;
            discount = result * 0.3;
            result -= discount;
        }
        else if (nights >= 10 & nights <= 15) {
            result = nights * 25;
            discount = result * 0.35;
            result -= discount;
        }
        else if (nights > 15) {
            result = nights * 25;
            discount = result * 0.5;
            result -= discount;
        }

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    else if (type_room == 'president apartment') {
        if (nights < 10) {
            result = nights * 35;
            discount = result * 0.1;
            result -= discount;
        }
        else if (nights >= 10 & nights <= 15) {
            result = nights * 35;
            discount = result * 0.15;
            result -= discount;
        }
        else if (nights > 15) {
            result = nights * 35;
            discount = result * 0.2;
            result -= discount;
        }

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    result = (result).toFixed(2);
    console.log(result);
}


