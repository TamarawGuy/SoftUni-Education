function old_books(input) {
    let favoite_book = input[0];
    let data = input[1];
    let index = 2;
    let searched_books = 0;
    let found = false;

    while (data !== "No More Books") {
        if (data !== favoite_book) {
            searched_books++;
        }
        else {
            found = true;
            break;
        }
        data = input[index];
        index++;
    }
    if (found) {
        console.log(`You checked ${searched_books} books and found it.`);
    }
    else {
        console.log("The book you search is not here!");
        console.log(`You checked ${searched_books} books.`);
    }
}