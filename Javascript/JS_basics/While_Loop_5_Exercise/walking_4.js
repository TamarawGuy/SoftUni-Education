function steps(input) {
    let result = 0;

    for (let i = 0; i < input.length; i++) {
        let data = input[i];
        if (data === 'Going home') {
            continue;
        }
        else {
            let steps = Number(input[i]);
            result += steps;
        }
    }
    if (result >= 10000) {
        steps_over = result - 10000;
        console.log(`Goal reached! Good job!`);
        console.log(`${steps_over} steps over the goal!`)
    }
    else {
        steps_need = 10000 - result;
        console.log(`${steps_need} more steps to reach goal.`)
    }
}