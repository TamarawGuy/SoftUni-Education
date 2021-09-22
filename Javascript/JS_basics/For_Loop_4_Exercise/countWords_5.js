function countWords(input) {
    let string = input[0];
    let arr = string.split(" ");

    if (arr.length <= 10) {
        console.log("The message was sent successfully!");
    }
    else {
        console.log(`The message is too long to be send! Has ${arr.length} words.`);
    }
}