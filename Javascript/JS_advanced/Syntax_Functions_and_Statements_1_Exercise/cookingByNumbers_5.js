function cookingByNumbers(num, op1, op2, op3, op4, op5) {
    let number = Number(num);
    let arr = [op1, op2, op3, op4, op5];

    for (const item of arr) {
        if (item === 'chop') {
            number /= 2;
            console.log(number);
        }
        else if (item === 'dice') {
            number = Math.sqrt(number);
            console.log(number);
        }
        else if (item === 'spice') {
            number += 1;
            console.log(number);
        }
        else if (item === 'bake') {
            number *= 3;
            console.log(number);
        }
        else if (item === 'fillet') {
            number -= number * 0.2;
            console.log(number);
        }
    }
}