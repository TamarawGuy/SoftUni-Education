function sortByTwoCriteria(arr) {
    newArr = arr.sort(function (a, b) {
        return a.length - b.length || a.localeCompare(b);
    });
    return newArr.join('\n');
}
