function holiday(input) {
    let nights = Number(input[0]) - 1;
    let type_room = input[1];
    let grade = input[2];
    let result;
    let discount;

    if (type_room == 'room for one person') {
        result = nights * 18;

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    else if (type_room == 'apartment') {
        if (nights < 10) {
            result = nights * 25;
            discount = result * 0.3;
            result -= discount;
        }
        else if (nights >= 10 & nights <= 15) {
            result = nights * 25;
            discount = result * 0.35;
            result -= discount;
        }
        else if (nights > 15) {
            result = nights * 25;
            discount = result * 0.5;
            result -= discount;
        }

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    else if (type_room == 'president apartment') {
        if (nights < 10) {
            result = nights * 35;
            discount = result * 0.1;
            result -= discount;
        }
        else if (nights >= 10 & nights <= 15) {
            result = nights * 35;
            discount = result * 0.15;
            result -= discount;
        }
        else if (nights > 15) {
            result = nights * 35;
            discount = result * 0.2;
            result -= discount;
        }

        if (grade == 'positive') {
            result += result * 0.25;
        }
        else {
            result -= result * 0.1;
        }
    }
    result = (result).toFixed(2);
    console.log(result);
}