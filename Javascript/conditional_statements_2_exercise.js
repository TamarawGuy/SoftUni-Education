function sumMinutes(input) {
    let num1 = Number(input[0])
    let num2 = Number(input[1])
    let num3 = Number(input[2])

    let total_seconds = num1 + num2 + num3;
    let minutes = 0;

    while (total_seconds >= 60) {
        total_seconds -= 60;
        minutes += 1;
    }
    if (total_seconds >= 10) {
        console.log(`${minutes}:${total_seconds}`);
    }
    else {
        console.log(`${minutes}:0${total_seconds}`);
    }
}

function bonusPoints(input) {
    let num = Number(input[0]);
    let bonus = 0.0;

    if (num <= 100) {
        bonus += 5;
    }
    else if (num > 100 && num <= 1000) {
        bonus = num * 0.2;
    }
    else {
        bonus = num * 0.1;
    }

    if (num % 2 == 0) {
        bonus += 1;
    }
    else if (num % 10 == 5) {
        bonus += 2;
    }
    console.log(bonus);
    console.log(bonus + num)
}

function speedInfo(input) {
    let num = Number(input[0]);

    if (num <= 10) {
        console.log('slow');
    }
    else if (num > 10 && num <= 50) {
        console.log('average');
    }
    else if (num > 50 && num <= 150) {
        console.log('fast');
    }
    else if (num > 150 && num <= 1000) {
        console.log('ultra fast');
    }
    else {
        console.log('extremely fast');
    }
}

function metricConverter(input) {
    let num = Number(input[0]);
    let from = input[1];
    let to = input[2];
    let result;

    if (from == 'mm' && to == 'cm') {
        result = (num / 10).toFixed(3);
    }
    else if (from == 'cm' && to == 'mm') {
        result = (num * 10).toFixed(3);
    }

    else if (from == 'cm' && to == 'm') {
        result = (num / 100).toFixed(3);
    }
    else if (from == 'm' && to == 'cm') {
        result = (num * 100).toFixed(3);
    }

    else if (from == 'mm' && to == 'm') {
        result = (num / 1000).toFixed(3);
    }
    else if (from == 'm' && to == 'mm') {
        result = (num * 1000).toFixed(3);
    }
    console.log(result);
}

function timePlus15Minutes(input) {
    let hour = Number(input[0]);
    let minutes = Number(input[1]);

    if (hour <= 22) {
        minutes += 15;
        if (minutes + 15 >= 60) {
            minutes -= 60;
            hour += 1;
        }
    }
    else if (hour == 23) {
        minutes += 15;
        if (minutes >= 60) {
            minutes -= 60;
            hour = 0;
        }
    }

    if (minutes < 10) {
        console.log(`${hour}:0${minutes}`);
    }
    else {
        console.log(`${hour}:${minutes}`);
    }
}


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


function swim(input) {
    let record_seconds = Number(input[0]);
    let distance = Number(input[1]);
    let meter_time = Number(input[2]);

    let seconds = distance * meter_time;
    let bonus = distance / 15 * 12.5;
    let total = (seconds + bonus).toFixed(2);

    if (record_seconds > total) {
        console.log(`Yes, he succeeded! The new world record is ${total} seconds.`)
    }
    else {
        let seconds_left = (total - record_seconds).toFixed(2);
        console.log(`No, he failed! He was ${seconds_left} seconds slower.`)
    }
}