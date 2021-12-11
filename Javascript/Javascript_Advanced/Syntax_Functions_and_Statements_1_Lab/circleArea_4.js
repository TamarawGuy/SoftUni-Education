function circleArea(input) {
    let type = typeof (input);
    if (type !== 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${type}.`);
    }
    else {
        let area = Math.PI * input * input;
        console.log(area.toFixed(2));
    }
}