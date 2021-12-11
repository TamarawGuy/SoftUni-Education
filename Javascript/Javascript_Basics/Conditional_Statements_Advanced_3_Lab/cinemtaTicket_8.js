function cinemaTicket(input) {
    let day = input[0];

    if (day == 'Saturday' || day == 'Sunday') {
        console.log(16);
    }
    else if (day == 'Wednesday' || day == 'Thursday') {
        console.log(14);
    }
    else {
        console.log(12);
    }
}