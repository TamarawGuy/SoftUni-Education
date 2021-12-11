
function equalNeightbours(matrix) {
    let counter = 0;

    for (let i = 0; i <= matrix.length - 2; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] === matrix[i + 1][j]) {
                counter++;
            }
        }
    }

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix.length - 1; j++) {
            if (matrix[i][j] === matrix[i][j + 1]) {
                counter++;
            }
        }
    }

    return counter;
}