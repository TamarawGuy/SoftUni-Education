function solve(input) {
    let result = [];

    let obj = {
        add,
        remove,
        print
    }

    function add(v) {
        result.push(v);
    }

    function remove(v) {
        result = result.filter(i => i !== v);
    }

    function print() {
        console.log(result.join(','));
    }

    input.forEach(pair => {
        const [command, value] = pair.split(' ');
        obj[command](value);
    });
}


solve(['add hello', 'add again', 'remove hello', 'add again', 'print']);