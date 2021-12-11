function leapYear(input) {
    let leap_year = Number(input[0]);
    let year = Number(input[1]);

    for (let i = leap_year; i <= year; i++) {
        if (i % 4 == 0) {
            console.log(i);
        }
    }
}