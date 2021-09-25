function carFactory(obj) {
    const newObj = {};

    newObj.model = obj.model;
    if (obj.power <= 90) {
        newObj.engine = {
            power: 90,
            volume: 1800,
        };
    }
    else if (obj.power > 90 && obj.power <= 120) {
        newObj.engine = {
            power: 120,
            volume: 2400,
        };
    }
    else if (obj.power > 120) {
        newObj.engine = {
            power: 200,
            volume: 3500
        };
    }

    if (obj.carriage === 'hatchback') {
        newObj.carriage = {
            type: 'hatchback',
            color: obj.color
        }
    }
    else if (obj.carriage === 'coupe') {
        newObj.carriage = {
            type: 'coupe',
            color: obj.color
        }
    }

    if (obj.wheelsize % 2 === 0) {
        const size = obj.wheelsize - 1;
        newObj.wheels = [size, size, size, size];
    }
    else {
        const size = obj.wheelsize;
        newObj.wheels = [size, size, size, size];
    }

    return newObj;
}