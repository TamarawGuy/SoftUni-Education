function calculateDeposits(input) {
    let deposit = Number(input[0])
    let months = Number(input[1])
    let apy = Number(input[2])

    let interest = deposit * apy / 100;
    let interestOneMonth = interest / 12;
    let total = deposit + (months * interestOneMonth);
    console.log(total);
}