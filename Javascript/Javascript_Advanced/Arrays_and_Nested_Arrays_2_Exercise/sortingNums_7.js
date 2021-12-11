function sortingNums(arr) {
    let newArr = [];
    arr.sort((a, b) => a - b);

    while (arr.length > 0) {
        newArr.push(arr.shift());
        newArr.push(arr.pop());
    }
    return newArr;
}