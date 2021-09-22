function sumLetters(input) {
    let word = input[0];
    let result = 0;

    for (let i = 0; i < word.length; i++) {
        if (word[i] == 'a') {
            result += 1;
        }
        else if (word[i] == 'e') {
            result += 2;
        }
        else if (word[i] == 'i') {
            result += 3;
        }
        else if (word[i] == 'o') {
            result += 4;
        }
        else if (word[i] == 'u') {
            result += 5;
        }
    }
    console.log(result);
}