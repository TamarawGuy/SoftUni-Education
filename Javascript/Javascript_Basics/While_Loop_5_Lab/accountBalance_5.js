function balance(input) {
    let data = input[0];
    let result = 0;
    let index = 1;

    while (data !== 'NoMoreMoney') {
        let money = Number(data);
        if (money < 0) {
            console.log("Invalid operation!");
            break;
        }
        result += money;
        console.log(`Increase: ${(money).toFixed(2)}`);
        data = input[index];
        index++;
    }
    result = (result).toFixed(2);
    console.log(`Total: ${result}`)
}