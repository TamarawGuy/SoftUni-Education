function shop(input) {
    let holiday = Number(input[0]);
    let puzzles = Number(input[1])
    let dolls = Number(input[2]);
    let bears = Number(input[3]);
    let minions = Number(input[4]);
    let trucks = Number(input[5]);

    total_sum_toys = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2;
    total_toys = puzzles + dolls + bears + minions + trucks;

    if (total_toys >= 50) {
        total_sum_toys -= total_sum_toys * 0.25;
    }

    total_sum_toys -= total_sum_toys * 0.1;

    if (total_sum_toys >= holiday) {
        let money_left = (total_sum_toys - holiday).toFixed(2);
        console.log(`Yes! ${money_left} lv left.`)
    }
    else {
        let money_needed = (holiday - total_sum_toys).toFixed(2);
        console.log(`Not enough money! ${money_needed} lv needed.`)
    }
}