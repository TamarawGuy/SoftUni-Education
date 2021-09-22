function sumNums(input) {
    let num = input[0];
    let result = 0;

    for (let i = 0; i < num.length; i++) {
        let number = Number(num[i]);
        result += number;
    }

    console.log(`The sum of the digits is:${result}`);
}