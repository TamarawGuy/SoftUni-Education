function sumSeconds(input) {
    let num1 = Number(input[0])
    let num2 = Number(input[1])
    let num3 = Number(input[2])

    let total_seconds = num1 + num2 + num3;
    let minutes = 0;

    while (total_seconds >= 60) {
        total_seconds -= 60;
        minutes += 1;
    }
    if (total_seconds >= 10) {
        console.log(`${minutes}:${total_seconds}`);
    }
    else {
        console.log(`${minutes}:0${total_seconds}`);
    }
}