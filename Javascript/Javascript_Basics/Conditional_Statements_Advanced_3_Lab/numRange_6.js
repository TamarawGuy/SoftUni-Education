function numInInterval(input) {
    let num = Number(input[0]);
    let result = 'No';

    if (num != 0) {
        if (num >= -100 && num <= 100) {
            result = 'Yes';
            console.log(result);
        }
        else {
            console.log(result);
        }
    }
    else {
        console.log(result);
    }
}