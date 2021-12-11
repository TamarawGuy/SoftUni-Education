function lastNumbersSequence(n, k) {
    function getSum(arr) {
        let sum = 0;

        for (let i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        return sum;
    }

    let counter = 0;
    let arr = [1];
    let numberToAdd;

    while (counter !== n - 1) {
        if (arr.length <= k) {
            numberToAdd = getSum(arr);
        }
        else {
            let lastKElements = arr.slice((arr.length - k), arr.length);
            numberToAdd = getSum(lastKElements);
        }
        arr.push(numberToAdd);
        counter++;
    }
    return arr;
}