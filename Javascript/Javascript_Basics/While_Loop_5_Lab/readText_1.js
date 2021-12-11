function readText(input) {
    let data = input[0];
    let index = 1;

    while (data !== 'Stop') {
        console.log(data);
        data = input[index];
        index++;
    }
}