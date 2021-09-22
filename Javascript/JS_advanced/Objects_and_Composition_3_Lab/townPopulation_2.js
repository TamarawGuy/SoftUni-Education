function population(townsArray) {
    const towns = {};

    for (let townAsString of townsArray) {
        let tokens = townAsString.split(' <-> ');
        let name = tokens[0];
        let population = Number(tokens[1]);
        if (towns[name] == undefined) {
            towns[name] = population;
        }
        else {
            towns[name] += population;
        }
    }

    for (const key in towns) {
        console.log(`${key} : ${towns[key]}`)
    }
}