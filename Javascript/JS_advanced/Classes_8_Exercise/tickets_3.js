function solve(arr, string) {
    let arrObj = [];

    arr.forEach(item => {
        let [destination, price, status] = item.split('|');
        price = Number(price);
        let obj = {
            destination,
            price,
            status
        };

        arrObj.push(obj);
    });

    if (string === 'destination') {
        return arrObj.sort((a, b) => a.destination.localeCompare(b.destination));
    }

    else if (string === 'price') {
        return arrObj.sort((a, b) => a.price - b.price);
    }

    else if (string === 'status') {
        return arrObj.sort((a, b) => a.status.localeCompare(b.status));
    }

}


console.log(solve(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'], 'status'));