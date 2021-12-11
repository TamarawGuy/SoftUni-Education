function sumNums(input) {
    let main_num = Number(input[0]);
    let result = 0;
    let data = Number(input[1]);
    let index = 2;

    while (result < main_num) {
        result += data;
        data = Number(input[index]);
        index++;
    }
    console.log(result);
}