function vacation(input) {
    let money_vacation = Number(input[0]);
    let current_money = Number(input[1]);
    let spend = 0;
    let save = 0;
    let data = input.slice(2);

    for (let i = 0; i < data.length; i++) {
        let item = data[i];

        if (item == 'spend') {
            let num = Number(data[i + 1]);
            current_money -= num;
            spend++;
            if (current_money < 0) {
                current_money = 0;
            }

            if (spend == 5) {
                console.log("You can't save the money.");
                console.log(`${spend + save}`);
                break;
            }
        }
        else if (item == 'save') {
            let num = Number(data[i + 1]);
            current_money += num;
            save++;
        }
        else {
            continue;
        }
    }
    if (current_money >= money_vacation) {
        console.log(`You saved the money for ${spend + save} days.`);
    }
}