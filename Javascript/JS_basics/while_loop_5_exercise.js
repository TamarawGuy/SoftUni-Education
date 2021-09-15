function old_books(input) {
    let favoite_book = input[0];
    let data = input[1];
    let index = 2;
    let searched_books = 0;
    let found = false;

    while (data !== "No More Books") {
        if (data !== favoite_book) {
            searched_books++;
        }
        else {
            found = true;
            break;
        }
        data = input[index];
        index++;
    }
    if (found) {
        console.log(`You checked ${searched_books} books and found it.`);
    }
    else {
        console.log("The book you search is not here!");
        console.log(`You checked ${searched_books} books.`);
    }
}

function exam_preparation(input) {
    let limit_poor_grades = Number(input[0]);
    let data = input[1];
    let index = 1;
    let result = 0;
    let problems = 0;
    let poor_grades = 0;
    let fail = false;

    while (data !== 'Enough') {
        problems += 1;
        last_problem = data;
        let grade = Number(input[index + 1]);
        if (grade <= 4) {
            poor_grades++;
            result += grade;
        }
        else {
            result += grade;
        }

        if (poor_grades === limit_poor_grades) {
            console.log(`You need a break, ${limit_poor_grades} poor grades.`);
            fail = true;
            break;
        }
        index += 2;
        data = input[index];
    }

    let average = (result / problems).toFixed(2);
    if (!fail) {
        console.log(`Average score: ${average}`);
        console.log(`Number of problems: ${problems}`);
        console.log(`Last problem: ${last_problem}`);
        console.log(`Last problem: ${last_problem}`);
    }
}

function vacation(input) {
    let money_vacation = Number(input[0]);
    let current_money = Number(input[1]);
    let spend = 0;
    let save = 0;
    let data = input.slice(2);

    for (let i = 0; i < data.length; i++) {
        let item = data[i];

        if (item == 'spend') {
            let num = Number(data[i + 1]);
            current_money -= num;
            spend++;
            if (current_money < 0) {
                current_money = 0;
            }

            if (spend == 5) {
                console.log("You can't save the money.");
                console.log(`${spend + save}`);
                break;
            }
        }
        else if (item == 'save') {
            let num = Number(data[i + 1]);
            current_money += num;
            save++;
        }
        else {
            continue;
        }
    }
    if (current_money >= money_vacation) {
        console.log(`You saved the money for ${spend + save} days.`);
    }
}

function steps(input) {
    let result = 0;

    for (let i = 0; i < input.length; i++) {
        let data = input[i];
        if (data === 'Going home') {
            continue;
        }
        else {
            let steps = Number(input[i]);
            result += steps;
        }
    }
    if (result >= 10000) {
        steps_over = result - 10000;
        console.log(`Goal reached! Good job!`);
        console.log(`${steps_over} steps over the goal!`)
    }
    else {
        steps_need = 10000 - result;
        console.log(`${steps_need} more steps to reach goal.`)
    }
}

function vendingMachine(input) {
    let coin_change = Math.floor(Number(input[0]) * 100);
    let coins = 0;

    while (coin_change > 0) {
        if (coin_change >= 200) coin_change -= 200;
        else if (coin_change >= 100) coin_change -= 100;
        else if (coin_change >= 50) coin_change -= 50;
        else if (coin_change >= 20) coin_change -= 20;
        else if (coin_change >= 10) coin_change -= 10;
        else if (coin_change >= 5) coin_change -= 5;
        else if (coin_change >= 2) coin_change -= 2;
        else coin_change -= 1;
        coins++;
    }
    console.log(coins);
}

function cake(input) {
    let cake = Number(input[0]) * Number(input[1]);
    let data = input[2];
    let index = 3;
    let ok = true;

    let result = 0;
    while (data !== 'STOP') {
        let num = Number(data);
        result += num;
        if (result > cake) {
            ok = false
            break;
        }
        data = input[index];
        index++;
    }

    if (!ok) {
        pieces_more = result - cake;
        console.log(`No more cake left! You need ${pieces_more} pieces more.`);
    }
    else {
        pieces_left = cake - result;
        console.log(`${pieces_left} pieces are left.`)
    }
}