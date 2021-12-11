function exam_preparation(input) {
    let limit_poor_grades = Number(input[0]);
    let data = input[1];
    let index = 1;
    let result = 0;
    let problems = 0;
    let poor_grades = 0;
    let fail = false;

    while (data !== 'Enough') {
        problems += 1;
        last_problem = data;
        let grade = Number(input[index + 1]);
        if (grade <= 4) {
            poor_grades++;
            result += grade;
        }
        else {
            result += grade;
        }

        if (poor_grades === limit_poor_grades) {
            console.log(`You need a break, ${limit_poor_grades} poor grades.`);
            fail = true;
            break;
        }
        index += 2;
        data = input[index];
    }

    let average = (result / problems).toFixed(2);
    if (!fail) {
        console.log(`Average score: ${average}`);
        console.log(`Number of problems: ${problems}`);
        console.log(`Last problem: ${last_problem}`);
        console.log(`Last problem: ${last_problem}`);
    }
}