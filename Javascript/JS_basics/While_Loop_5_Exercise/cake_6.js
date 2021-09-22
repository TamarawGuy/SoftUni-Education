function cake(input) {
    let cake = Number(input[0]) * Number(input[1]);
    let data = input[2];
    let index = 3;
    let ok = true;

    let result = 0;
    while (data !== 'STOP') {
        let num = Number(data);
        result += num;
        if (result > cake) {
            ok = false
            break;
        }
        data = input[index];
        index++;
    }

    if (!ok) {
        pieces_more = result - cake;
        console.log(`No more cake left! You need ${pieces_more} pieces more.`);
    }
    else {
        pieces_left = cake - result;
        console.log(`${pieces_left} pieces are left.`)
    }
}