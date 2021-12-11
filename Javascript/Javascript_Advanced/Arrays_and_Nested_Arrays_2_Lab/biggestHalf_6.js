function biggerHalf(arr) {
    arr.sort((a, b) => a - b);
    let index = Math.floor(arr.length / 2);
    let firstHalf = arr.slice(0, index);
    let secondHalf = arr.slice(index);

    if (firstHalf.length <= secondHalf.length) {
        return secondHalf;
    }
    else if (firstHalf.length > secondHalf.length) {
        return firstHalf;
    }
}