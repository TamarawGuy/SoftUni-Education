function from1To100(input) {
    for (let i = 1; i <= 100; i++) {
        console.log(i);
    }
}

function fromNto1(input) {
    let = Number(input[0]);

    for (let i = n; i > 0; i--) {
        console.log(i);
    }
}

function from1ToNstep3(input) {
    let num = Number(input[0]);

    for (let i = 1; i <= n; i += 3) {
        console.log(i);
    }
}

function evenSteps(input) {
    let n = Number(input[0]);

    for (let i = 0; i < n; i += 2) {
        console.log(Math.pow(2, i));
    }
}

function symbols(input) {
    let text = input[0];
    for (let i = 0; i < text.length; i++) {
        console.log(text[i]);
    }
}

function sumLetters(input) {
    let word = input[0];
    let result = 0;

    for (let i = 0; i < word.length; i++) {
        if (word[i] == 'a') {
            result += 1;
        }
        else if (word[i] == 'e') {
            result += 2;
        }
        else if (word[i] == 'i') {
            result += 3;
        }
        else if (word[i] == 'o') {
            result += 4;
        }
        else if (word[i] == 'u') {
            result += 5;
        }
    }
    console.log(result);
}

function sumNums(input) {
    let num = input[0];
    let result = 0;

    for (let i = 0; i < num.length; i++) {
        let number = Number(num[i]);
        result += number;
    }

    console.log(`The sum of the digits is:${result}`);
}

function numbers(input) {
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let result = 0;

    for (let i = num1; i <= num2; i++) {
        if (i % 9 == 0) {
            result += i;
        }
    }

    console.log(`The sum: ${result}`)

    for (let i = num1; i <= num2; i++) {
        if (i % 9 == 0) {
            console.log(i);
        }
    }
}

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

