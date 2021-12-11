function cinema(input) {
    let type = input[0];
    let rows = Number(input[1]);
    let cols = Number(input[2]);
    let result;

    if (type == 'Premiere') {
        result = rows * cols * 12;
    }
    else if (type == 'Normal') {
        result = rows * cols * 7.5;
    }
    else if (type == 'Discount') {
        result = rows * cols * 5;
    }
    result = (result).toFixed(2);
    console.log(`${result} leva`)
}