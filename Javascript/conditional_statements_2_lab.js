function excellentGrade(input) {
    let grade = Number(input[0]);
    if (grade >= 5.5) {
        console.log('Excellent!');
    }
}

function biggerNum(input) {
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);

    if (num1 >= num2) {
        console.log(num1);
    }
    else {
        console.log(num2);
    }
}

function oddOrEven(input) {
    let num = Number(input[0]);

    if (num % 2 == 0) {
        console.log('even');
    }
    else {
        console.log('odd');
    }
}

function numBetween100And200(input) {
    let num = Number(input[0]);

    if (num < 100) {
        console.log('Less than 100')
    }
    else if (num >= 100 && num <= 200) {
        console.log('Between 100 and 200')
    }
    else {
        console.log('Greater than 200');
    }
}

function guessPasword(input) {
    password = input[0];
    if (password == 's3cr3t!P@ssw0rd') {
        console.log('Welcome');
    }
    else {
        console.log('Wrong password!')
    }
}

function areaFigures(input) {
    let shape = input[0];
    let area;
    if (shape == 'square') {
        let side = Number(input[1]);
        area = side * side;
    }
    else if (shape == 'rectangle') {
        let length = Number(input[1]);
        let width = Number(input[2]);
        area = length * width;
    }
    else if (shape == 'circle') {
        let radius = Number(input[1]);
        area = radius * radius * Math.PI;
    }
    else if (shape == 'triangle') {
        let side1 = Number(input[1]);
        let side2 = Number(input[2]);
        area = side1 * side2 / 2;
    }
    console.log(area);
}

areaFigures(['square', '5'])

function shop(input) {
    let holiday = Number(input[0]);
    let puzzles = Number(input[1])
    let dolls = Number(input[2]);
    let bears = Number(input[3]);
    let minions = Number(input[4]);
    let trucks = Number(input[5]);

    total_sum_toys = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2;
    total_toys = puzzles + dolls + bears + minions + trucks;

    if (total_toys >= 50) {
        total_sum_toys -= total_sum_toys * 0.25;
    }

    total_sum_toys -= total_sum_toys * 0.1;

    if (total_sum_toys >= holiday) {
        let money_left = (total_sum_toys - holiday).toFixed(2);
        console.log(`Yes! ${money_left} lv left.`)
    }
    else {
        let money_needed = (holiday - total_sum_toys).toFixed(2);
        console.log(`Not enough money! ${money_needed} lv needed.`)
    }
}