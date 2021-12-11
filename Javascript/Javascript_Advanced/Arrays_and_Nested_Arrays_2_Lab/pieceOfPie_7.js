function pieceOfPie(arr, start, end) {
    let indexStart = arr.indexOf(start);
    let indexEnd = arr.indexOf(end);
    let newArr = arr.slice(indexStart, indexEnd + 1);

    return newArr;
}