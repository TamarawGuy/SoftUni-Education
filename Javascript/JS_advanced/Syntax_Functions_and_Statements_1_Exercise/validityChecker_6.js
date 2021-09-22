function validityChecker(x1, y1, x2, y2) {
    function findDistance(p1, p2, p3 = 0, p4 = 0) {
        let line = (p3 - p1) ** 2 + (p4 - p2) ** 2;
        let result = Math.sqrt(line);
        return result;
    }

    let r1 = findDistance(x1, y1);
    let r2 = findDistance(x2, y2);
    let r3 = findDistance(x1, y1, x2, y2);

    if (r1 % 1 == 0) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }

    if (r2 % 1 == 0) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }

    if (r3 % 1 == 0) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}