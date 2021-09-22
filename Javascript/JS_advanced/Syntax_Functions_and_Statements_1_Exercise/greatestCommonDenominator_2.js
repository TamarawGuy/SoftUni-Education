function gcd(num1, num2) {
    let result;

    for (let i = 1; i <= Math.min(num1, num2); i++) {
        if (num1 % i === 0 && num2 % i === 0) {
            result = i;
        }
    }
    console.log(result)
}