function negativePositiveNums(arr) {
    let newArr = [];

    for (const item of arr) {
        if (item >= 0) {
            newArr.push(item);
        }
        else {
            newArr.unshift(item);
        }
    }

    for (const num of newArr) {
        console.log(num);
    }
}