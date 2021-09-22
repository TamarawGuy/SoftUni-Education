function smallestNumber(input) {
    data = input[0];
    let smallest_num = 100000000000000;
    index = 1;

    while (data !== 'Stop') {
        let num = Number(data);
        if (num < smallest_num) {
            smallest_num = num;
        }
        data = input[index];
        index++;
    }
    console.log(smallest_num);
}