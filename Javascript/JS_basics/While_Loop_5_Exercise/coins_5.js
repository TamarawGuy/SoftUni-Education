function vendingMachine(input) {
    let coin_change = Math.floor(Number(input[0]) * 100);
    let coins = 0;

    while (coin_change > 0) {
        if (coin_change >= 200) coin_change -= 200;
        else if (coin_change >= 100) coin_change -= 100;
        else if (coin_change >= 50) coin_change -= 50;
        else if (coin_change >= 20) coin_change -= 20;
        else if (coin_change >= 10) coin_change -= 10;
        else if (coin_change >= 5) coin_change -= 5;
        else if (coin_change >= 2) coin_change -= 2;
        else coin_change -= 1;
        coins++;
    }
    console.log(coins);
}