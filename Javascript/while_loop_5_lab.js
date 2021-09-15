function readText(input) {
    let data = input[0];
    let index = 1;

    while (data !== 'Stop') {
        console.log(data);
        data = input[index];
        index++;
    }
}

function password(input) {
    let username = input[0];
    let password = input[1];
    let data = input[2];
    let index = 3;

    while (data !== password) {
        data = input[index];
        index++;
    }
    console.log(`Welcome ${username}!`);
}

function sumNums(input) {
    let main_num = Number(input[0]);
    let result = 0;
    let data = Number(input[1]);
    let index = 2;

    while (result < main_num) {
        result += data;
        data = Number(input[index]);
        index++;
    }
    console.log(result);
}

function seq2k_1(input) {
    let num = Number(input[0]);
    let result = 0;

    while (result < num - 1) {
        result = 2 * result + 1;
        console.log(result);
    }
}

function balance(input) {
    let data = input[0];
    let result = 0;
    let index = 1;

    while (data !== 'NoMoreMoney') {
        let money = Number(data);
        if (money < 0) {
            console.log("Invalid operation!");
            break;
        }
        result += money;
        console.log(`Increase: ${(money).toFixed(2)}`);
        data = input[index];
        index++;
    }
    result = (result).toFixed(2);
    console.log(`Total: ${result}`)
}

function biggestNumber(input) {
    data = input[0];
    let biggest_num = -100000000000000;
    index = 1;

    while (data !== 'Stop') {
        let num = Number(data);
        if (num > biggest_num) {
            biggest_num = num;
        }
        data = input[index];
        index++;
    }
    console.log(biggest_num);
}

function smallestNumber(input) {
    data = input[0];
    let smallest_num = 100000000000000;
    index = 1;

    while (data !== 'Stop') {
        let num = Number(data);
        if (num < smallest_num) {
            smallest_num = num;
        }
        data = input[index];
        index++;
    }
    console.log(smallest_num);
}

function graduate(input) {
    let name = input[0];
    let data = Number(input[1]);
    let index = 2;
    let fail = 0;
    let result = 0;
    let grade = 1;

    while (grade <= 12) {
        if (data >= 4) {
            result += data;
            data = Number(input[index]);
            index++;
            grade++;
        }
        else {
            fail++;
            if (fail > 1) {
                console.log(`${name} has been excluded at ${grade - 1} grade`);
                break;
            }
            result += data;
            data = Number(input[index]);
            index++;
            grade++;
        }
    }
    if (grade == 13) {
        let average = (result / 12).toFixed(2);
        console.log(`${name} graduated. Average grade: ${average}`);
    }
}