function factorial(input) {
    let num = Number(input[0]);
    let start = 1;
    let result = 1;

    for (let i = 1; i <= num; i++) {
        result *= i;
    }

    console.log(result);
}