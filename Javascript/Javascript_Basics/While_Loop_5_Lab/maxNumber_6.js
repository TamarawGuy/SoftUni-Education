function biggestNumber(input) {
    data = input[0];
    let biggest_num = -100000000000000;
    index = 1;

    while (data !== 'Stop') {
        let num = Number(data);
        if (num > biggest_num) {
            biggest_num = num;
        }
        data = input[index];
        index++;
    }
    console.log(biggest_num);
}