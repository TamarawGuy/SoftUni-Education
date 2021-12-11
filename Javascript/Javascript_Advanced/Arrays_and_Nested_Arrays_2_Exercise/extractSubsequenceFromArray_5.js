function extractNums(arr) {
    let newArr = [];
    let biggest = -1000000000000000;

    arr.reduce(function (acc, v) {
        if (v > biggest) {
            biggest = v;
            newArr.push(biggest);
        }
    }, biggest);

    return newArr;
}