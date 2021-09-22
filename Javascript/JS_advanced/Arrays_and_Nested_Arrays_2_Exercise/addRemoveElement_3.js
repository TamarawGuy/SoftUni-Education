function addRemoveElement(arr) {
    let newArr = [];
    let counter = 1;

    for (const item of arr) {
        if (item === 'add') {
            newArr.push(counter);
            counter++;
        }
        else if (item === 'remove') {
            if (newArr.length === 0) {
                continue;
            }
            else {
                newArr.pop();
                counter++;
            }
        }
    }

    if (newArr.length === 0) {
        return 'Empty';
    }
    else {
        return newArr.join('\n');
    }
}