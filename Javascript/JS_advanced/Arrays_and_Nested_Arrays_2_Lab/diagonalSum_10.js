function diagonalSums(matrix) {
    let firstDiagonalSum = 0;
    let secondDiagonalSum = 0;
    let counter = 0;

    for (let i = 0; i < matrix.length; i++) {
        firstDiagonalSum += matrix[i][i];
    }

    for (let i = matrix.length - 1; i >= 0; i--) {
        secondDiagonalSum += matrix[counter][i];
        counter++;
    }
    console.log(firstDiagonalSum, secondDiagonalSum);
}