function townsToJSON(arr) {
    let cleanData = [];
    let objects = [];

    for (let i = 0; i < arr.length; i++) {
        let cleanedItem = arr[i].substring(2, arr[i].length - 2);
        cleanData.push(cleanedItem);
    }

    for (let i = 1; i < cleanData.length; i++) {
        let [name, latitude, longitude] = cleanData[i].split(' | ');
        latitude = Math.round(Number(latitude) * 100) / 100;
        longitude = Math.round(Number(longitude) * 100) / 100;

        let obj = {
            Town: name,
            Latitude: latitude,
            Longitude: longitude
        };
        objects.push(obj);
    }


    console.log(JSON.stringify(objects));
}
