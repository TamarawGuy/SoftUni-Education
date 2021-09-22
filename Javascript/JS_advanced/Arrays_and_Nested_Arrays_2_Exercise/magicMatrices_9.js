function magicMatrices(matrix) {
    function getSum(row) {
        let s = row.reduce(function (acc, v) {
            return acc + v;
        }, 0);
        return s;
    }

    let isMagic = true;
    let mySum = getSum(matrix[0]);

    for (const row of matrix) {
        let sum = getSum(row);
        if (sum !== mySum) {
            isMagic = false;
            break;
        }
        else {
            continue;
        }
    }

    for (let i = 0; i < matrix[0].length; i++) {
        let col = matrix.map(d => d[i]);
        let sum = getSum(col);
        if (sum !== mySum) {
            isMagic = false;
            break;
        }
        else {
            continue;
        }
    }
    return isMagic;
}