function factory(library, orders) {
    const result = [];
    // iterate over orders
    for (let order of orders) {
        // copy order templates
        const composed = Object.assign({}, order.template);
        // compose methods by part list
        for (let part of order.parts) {
            composed[part] = library[part];
        }
        result.push(composed);
    }
    return result;
}