function seq2k_1(input) {
    let num = Number(input[0]);
    let result = 0;

    while (result < num - 1) {
        result = 2 * result + 1;
        console.log(result);
    }
}