function numberEndingIn7(input) {
    for (let i = 7; i <= 997; i++) {
        if (i % 10 == 7) {
            console.log(i);
        }
    }
}

function multiplicationTable(input) {
    let num = Number(input[0]);

    for (let i = 1; i <= 10; i++) {
        let result = i * num;
        console.log(`${i} * ${num} = ${result}`)
    }
}

function leapYear(input) {
    let leap_year = Number(input[0]);
    let year = Number(input[1]);

    for (let i = leap_year; i <= year; i++) {
        if (i % 4 == 0) {
            console.log(i);
        }
    }
}

function factorial(input) {
    let num = Number(input[0]);
    let start = 1;
    let result = 1;

    for (let i = 1; i <= num; i++) {
        result *= i;
    }

    console.log(result);
}

function countWords(input) {
    let string = input[0];
    let arr = string.split(" ");

    if (arr.length <= 10) {
        console.log("The message was sent successfully!");
    }
    else {
        console.log(`The message is too long to be send! Has ${arr.length} words.`);
    }
}

function histogram(input) {
    let input_num = Number(input[0]);
    let arr = input;
    let below_200 = 0;
    let between_200_and_399 = 0;
    let between_400_and_599 = 0;
    let between_600_and_799 = 0;
    let above_800 = 0;

    for (let i = 1; i <= input_num; i++) {
        let num = Number(arr[i]);

        if (num < 200) {
            below_200 += 1;
        }
        else if (num >= 200 && num < 400) {
            between_200_and_399 += 1;
        }
        else if (num >= 400 && num < 600) {
            between_400_and_599 += 1
        }
        else if (num >= 600 && num < 800) {
            between_600_and_799 += 1
        }
        else if (num >= 800) {
            above_800 += 1;
        }
    }
    let p1 = (below_200 / input_num * 100).toFixed(2);
    let p2 = (between_200_and_399 / input_num * 100).toFixed(2);
    let p3 = (between_400_and_599 / input_num * 100).toFixed(2);
    let p4 = (between_600_and_799 / input_num * 100).toFixed(2);
    let p5 = (above_800 / input_num * 100).toFixed(2);

    console.log(`${p1}%`);
    console.log(`${p2}%`);
    console.log(`${p3}%`);
    console.log(`${p4}%`);
    console.log(`${p5}%`);
}

function smallestNum(input) {
    let num = Number(input[0]);
    let smallest_num = 100000000000000000;

    for (let i = 1; i <= num; i++) {
        let n = Number(input[i]);

        if (n < smallest_num) {
            smallest_num = n;
        }
    }

    console.log(smallest_num);
}