function aggregateElements(input) {
    let result1 = 0;
    let result2 = 0;

    for (let i = 0; i < input.length; i++) {
        result1 += input[i];
        result2 += 1 / input[i];
    }

    console.log(result1);
    console.log(result2);
    console.log(input.join(""));
}