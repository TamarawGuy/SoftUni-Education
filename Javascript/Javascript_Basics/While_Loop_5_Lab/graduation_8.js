function graduate(input) {
    let name = input[0];
    let data = Number(input[1]);
    let index = 2;
    let fail = 0;
    let result = 0;
    let grade = 1;

    while (grade <= 12) {
        if (data >= 4) {
            result += data;
            data = Number(input[index]);
            index++;
            grade++;
        }
        else {
            fail++;
            if (fail > 1) {
                console.log(`${name} has been excluded at ${grade - 1} grade`);
                break;
            }
            result += data;
            data = Number(input[index]);
            index++;
            grade++;
        }
    }
    if (grade == 13) {
        let average = (result / 12).toFixed(2);
        console.log(`${name} graduated. Average grade: ${average}`);
    }
}