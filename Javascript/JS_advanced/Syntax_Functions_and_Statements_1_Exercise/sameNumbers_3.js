function sameNumbers(num) {
    let arr = Array.from(String(num), Number);
    let same = true;
    let sum = 0;

    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] !== arr[i + 1]) {
            same = false;
        }
    }

    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    console.log(same);
    console.log(sum);
}