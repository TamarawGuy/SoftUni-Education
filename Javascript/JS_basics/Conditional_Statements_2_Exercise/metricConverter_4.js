function metricConverter(input) {
    let num = Number(input[0]);
    let from = input[1];
    let to = input[2];
    let result;

    if (from == 'mm' && to == 'cm') {
        result = (num / 10).toFixed(3);
    }
    else if (from == 'cm' && to == 'mm') {
        result = (num * 10).toFixed(3);
    }

    else if (from == 'cm' && to == 'm') {
        result = (num / 100).toFixed(3);
    }
    else if (from == 'm' && to == 'cm') {
        result = (num * 100).toFixed(3);
    }

    else if (from == 'mm' && to == 'm') {
        result = (num / 1000).toFixed(3);
    }
    else if (from == 'm' && to == 'mm') {
        result = (num * 1000).toFixed(3);
    }
    console.log(result);
}