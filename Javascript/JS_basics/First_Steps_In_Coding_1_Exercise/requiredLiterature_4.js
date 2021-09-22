function bookList(input) {
    let pages = Number(input[0]);
    let pages1Hour = Number(input[1]);
    let days = Number(input[2]);

    let totalHours = pages / pages1Hour;
    let hoursPerDay = totalHours / days;
    console.log(hoursPerDay);
}