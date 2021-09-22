////////////////////////////
/////// EXERCISE 10 ////////
////////////////////////////

function ticTacToe(moves) {
    function checkIfOWinner(b) {
        winner = false;
        if (b[0][0] === 'O' && b[0][1] == 'O' && b[0][2] === 'O') {
            winner = true;
        }
        else if (b[1][0] === 'O' && b[1][1] === 'O' && b[1][2] === 'O') {
            winner = true;
        }
        else if (b[2][0] === 'O' && b[2][1] === 'O' && b[2][2] === 'O') {
            winner = true;
        }

        else if (b[0][0] === 'O' && b[1][0] === 'O' && b[2][0] === 'O') {
            winner = true;
        }
        else if (b[0][1] === 'O' && b[1][1] === 'O' && b[2][1] === 'O') {
            winner = true;
        }
        else if (b[0][2] === 'O' && b[1][2] === 'O' && b[2][2] === 'O') {
            winner = true;
        }

        else if (b[0][0] === 'O' && b[1][1] === 'O' && b[2][2] === 'O') {
            winner = true;
        }
        else if (b[0][2] === 'O' && b[1][1] === 'O' && b[2][0] === 'O') {
            winner = true;
        }

        return winner;
    }

    function checkIfXWinner(b) {
        winner = false;
        if (b[0][0] === 'X' && b[0][1] == 'X' && b[0][2] === 'X') {
            winner = true;
        }
        else if (b[1][0] === 'X' && b[1][1] === 'X' && b[1][2] === 'X') {
            winner = true;
        }
        else if (b[2][0] === 'X' && b[2][1] === 'X' && b[2][2] === 'X') {
            winner = true;
        }

        else if (b[0][0] === 'X' && b[1][0] === 'X' && b[2][0] === 'X') {
            winner = true;
        }
        else if (b[0][1] === 'X' && b[1][1] === 'X' && b[2][1] === 'X') {
            winner = true;
        }
        else if (b[0][2] === 'X' && b[1][2] === 'X' && b[2][2] === 'X') {
            winner = true;
        }

        else if (b[0][0] === 'X' && b[1][1] === 'X' && b[2][2] === 'X') {
            winner = true;
        }
        else if (b[0][2] === 'X' && b[1][1] === 'X' && b[2][0] === 'X') {
            winner = true;
        }

        return winner;
    }

    let nextTurn = 'O';
    let winnerO = false;
    let winnerX = false;
    let board = [
        [false, false, false],
        [false, false, false],
        [false, false, false],
    ]

    for (let i = 0; i < moves.length; i++) {
        let move = moves[i];
        let r = Number(move[0]);
        let c = Number(move[2]);

        if (nextTurn === 'O') {
            if (board[r][c] !== 'O' || board[r][c] !== 'X') {
                board[r][c] = 'O';
                nextTurn = 'X';
                if (checkIfOWinner(board)) {
                    winnerO = true;
                    break;
                }
                else {
                    continue;
                }
            }
            else {
                console.log("This place is already taken. Please choose another!");
                continue;
            }
        }

        else {
            if (board[r][c] !== 'O' || board[r][c] !== 'X') {
                board[r][c] = 'X';
                nextTurn = 'O';
                if (checkIfXWinner(board)) {
                    winnerX = true;
                    break;
                }
                else {
                    continue;
                }
            }
            else {
                console.log("This place is already taken. Please choose another!");
                continue;
            }
        }
    }

    if (winnerO && !winnerX) {
        console.log("Player O wins!");
    }
    else if (!winnerO && winnerX) {
        console.log("Player X wins!");
    }
    else if (!winnerO && !winnerX) {
        console.log('The game ended! Nobody wins :(');
    }
}

ticTacToe(['0 1',
    '0 0',
    '0 2',
    '2 0',
    '1 0',
    '1 2',
    '1 1',
    '2 1',
    '2 2',
    '0 0'],
)

// ticTacToe(['0 0',
//     '0 0',
//     '1 1',
//     '0 1',
//     '1 2',
//     '0 2',
//     '2 2',
//     '1 2',
//     '2 2',
//     '2 1'],
// )