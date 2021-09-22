function biggestElement(matrix) {
    let biggestNum = -1000000000000000;
    for (const row of matrix) {
        for (const num of row) {
            if (num > biggestNum) {
                biggestNum = num;
            }
        }
    }
    return biggestNum;
}