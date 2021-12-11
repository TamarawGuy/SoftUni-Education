function areaFigures(input) {
    let shape = input[0];
    let area;
    if (shape == 'square') {
        let side = Number(input[1]);
        area = side * side;
    }
    else if (shape == 'rectangle') {
        let length = Number(input[1]);
        let width = Number(input[2]);
        area = length * width;
    }
    else if (shape == 'circle') {
        let radius = Number(input[1]);
        area = radius * radius * Math.PI;
    }
    else if (shape == 'triangle') {
        let side1 = Number(input[1]);
        let side2 = Number(input[2]);
        area = side1 * side2 / 2;
    }
    console.log(area);
}