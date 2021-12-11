function smallestNum(input) {
    let num = Number(input[0]);
    let smallest_num = 100000000000000000;

    for (let i = 1; i <= num; i++) {
        let n = Number(input[i]);

        if (n < smallest_num) {
            smallest_num = n;
        }
    }

    console.log(smallest_num);
}