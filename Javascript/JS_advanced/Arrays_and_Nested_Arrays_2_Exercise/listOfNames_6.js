function listOfNames(arr) {
    arr.sort((a, b) => a.localeCompare(b));
    arr.forEach(function (item, index) {
        console.log(`${index + 1}.${item}`);
    });
}