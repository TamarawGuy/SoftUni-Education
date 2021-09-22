function histogram(input) {
    let input_num = Number(input[0]);
    let arr = input;
    let below_200 = 0;
    let between_200_and_399 = 0;
    let between_400_and_599 = 0;
    let between_600_and_799 = 0;
    let above_800 = 0;

    for (let i = 1; i <= input_num; i++) {
        let num = Number(arr[i]);

        if (num < 200) {
            below_200 += 1;
        }
        else if (num >= 200 && num < 400) {
            between_200_and_399 += 1;
        }
        else if (num >= 400 && num < 600) {
            between_400_and_599 += 1
        }
        else if (num >= 600 && num < 800) {
            between_600_and_799 += 1
        }
        else if (num >= 800) {
            above_800 += 1;
        }
    }
    let p1 = (below_200 / input_num * 100).toFixed(2);
    let p2 = (between_200_and_399 / input_num * 100).toFixed(2);
    let p3 = (between_400_and_599 / input_num * 100).toFixed(2);
    let p4 = (between_600_and_799 / input_num * 100).toFixed(2);
    let p5 = (above_800 / input_num * 100).toFixed(2);

    console.log(`${p1}%`);
    console.log(`${p2}%`);
    console.log(`${p3}%`);
    console.log(`${p4}%`);
    console.log(`${p5}%`);
}