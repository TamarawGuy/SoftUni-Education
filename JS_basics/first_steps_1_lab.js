function hello(input) {
    console.log("Hello SoftUni");
}

function nums() {
    for (i = 1; i < 11; i++) {
        console.log(i);
    }
}

function squareArea(input) {
    let a = Number(input[0]);
    let area = a * a;
    console.log(area)
}

function fromInchesToCent(input) {
    let inch = Number(input[0]);
    let result = inch * 2.54;
    console.log(result)
}

function greetings(input) {
    let name = input[0];
    console.log(`Hello, ${name}!`);
}

function concatData(input) {
    console.log(`You are ${input[0]} ${input[1]}, a ${Number(input[2])}-years old person from ${input[3]}.`)
}

function projects(input) {
    let hours = Number(input[1]) * 3;
    console.log(`The architect ${input[0]} will need ${hours} hours to complete ${input[1]} project/s.`)
}

function zoo(input) {
    let dogFood = Number(input[0]) * 2.5;
    let food = Number(input[1]) * 4;
    console.log(`${dogFood + food} lv.`)
}

function yardGreening(input) {
    let num = Number(input[0]);
    let price = num * 7.61;
    let discount = price * 0.18;
    let totalPrice = price - discount;
    console.log(`The final price is: ${totalPrice} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}
