function swim(input) {
    let record_seconds = Number(input[0]);
    let distance = Number(input[1]);
    let meter_time = Number(input[2]);

    let seconds = distance * meter_time;
    let bonus = distance / 15 * 12.5;
    let total = (seconds + bonus).toFixed(2);

    if (record_seconds > total) {
        console.log(`Yes, he succeeded! The new world record is ${total} seconds.`)
    }
    else {
        let seconds_left = (total - record_seconds).toFixed(2);
        console.log(`No, he failed! He was ${seconds_left} seconds slower.`)
    }
}