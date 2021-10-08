function solve(input, criteria) {
    let data = JSON.parse(input);

    if (criteria === 'all') {
        for (let [index, person] of data.entries()) {
            console.log(`${index}. ${person.first_name} ${person.last_name} - ${person.email}`);
        }
    }
    else {
        let [key, value] = criteria.split('-');

        for (let i = 0; i < data.length; i++) {
            let person = data[i];
            if (person[key] === value) {
                console.log(`${i}. ${person.first_name} ${person.last_name} - ${person.email}`);
            }

        }
    }
}

solve(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`,
    'gender-Female'
)