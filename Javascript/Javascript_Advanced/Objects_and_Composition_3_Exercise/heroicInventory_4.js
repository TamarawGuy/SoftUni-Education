function heroicInventory(arrStr) {
    let result = [];

    for (const item of arrStr) {
        let [name, level, items] = item.split(' / ');
        level = Number(level);
        items = items ? items.split(', ') : [];
        result.push({ name, level, items });
    }
    console.log(JSON.stringify(result));
}