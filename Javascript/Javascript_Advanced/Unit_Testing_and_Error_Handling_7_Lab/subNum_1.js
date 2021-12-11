function sumSub(arr, start, end) {
    // take range of array
    // sum selected el
    if (Array.isArray(arr) == false) {
        return NaN;
    }

    if (start < 0) {
        start = 0;
    }

    if (end > arr.length - 1) {
        end = arr.length - 1;
    }

    let sum = 0;

    for (let i = start; i <= end; i++) {
        sum += Number(arr[i]);
    }

    //return result
    return sum;
}

console.log(sumSub([10, 20, 30, 40, 50, 60], 3, 300));
console.log(sumSub([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1));
console.log(sumSub([10, 'twenty', 30, 40], 0, 2));
console.log(sumSub([], 1, 2));
console.log(sumSub('text', 0, 2));
