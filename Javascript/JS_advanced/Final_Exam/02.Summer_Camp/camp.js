class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = { 'child': 150, 'student': 300, 'collegian': 500 };
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        if (!Object.keys(this.priceForTheCamp).includes(condition)) {
            throw new Error('Unsuccessful registration at the camp.');
        }

        for (const obj of this.listOfParticipants) {
            if (obj.name === name) {
                return `The ${name} is already registered at the camp.`;
            }
        }

        if (money < this.priceForTheCamp[condition]) {
            return "The money is not enough to pay the stay at the camp.";
        }

        let child = {
            name,
            condition,
            power: 100,
            wins: 0
        };

        this.listOfParticipants.push(child);
        return `The ${name} was successfully registered.`
    }

    unregisterParticipant(name) {
        let found = false;

        for (let person of this.listOfParticipants) {
            if (person.name === name) {
                let index = this.listOfParticipants.indexOf(person);
                this.listOfParticipants.splice(index, 1);
                found = true;
                return `The ${name} removed successfully.`;
            }
        }

        if (found === false) {
            throw new Error(`The ${name} is not registered in the camp.`);
        }
    }

    timeToPlay(typeOfGame, participant1, participant2) {
        if (typeOfGame === 'WaterBalloonFights') {
            let found1 = false;
            let found2 = false;

            for (const person of this.listOfParticipants) {
                if (person.name === participant1) {
                    found1 = true;
                }

                if (person.name === participant2) {
                    found2 = true;
                }
            }
            if (found1 == false || found2 == false) {
                throw new Error('Invalid entered name/s.');
            }
            else {
                let person1 = this.listOfParticipants.find(p => p.name === participant1);
                let person2 = this.listOfParticipants.find(p => p.name === participant2);
                if (person1.condition !== person2.condition) {
                    throw new Error('Choose players with equal condition.');
                }
                else {
                    if (person1.power > person2.power) {
                        this.listOfParticipants.forEach(p => {
                            if (p === person1) {
                                p.wins += 1;
                            }
                        });
                        return `The ${person1.name} is winner in the game ${typeOfGame}.`;
                    }
                    else if (person1.power < person2.power) {
                        this.listOfParticipants.forEach(p => {
                            if (p === person2) {
                                p.wins += 1;
                            }
                        });
                        return `The ${person2.name} is winner in the game ${typeOfGame}.`;
                    }
                    else {
                        return 'There is no winner.';
                    }
                }
            }
        }
        else {
            let found1 = false;
            for (const person of this.listOfParticipants) {
                if (person.name === participant1) {
                    found1 = true;
                }
            }
            if (found1 == false) {
                throw new Error('Invalid entered name/s.');
            }
            else {
                this.listOfParticipants.forEach(p => {
                    if (p.name === participant1) {
                        p.power += 20;
                    }
                });
                return `The ${participant1} successfully completed the game ${typeOfGame}.`;
            }
        }
    }

    toString() {
        let result = '';
        result += `${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}` + '\n';
        this.listOfParticipants.sort((a, b) => b.wins - a.wins);
        this.listOfParticipants.forEach(p => {
            result += `${p.name} - ${p.condition} - ${p.power} - ${p.wins}` + '\n';
        });
        result = result.slice(0, -1);

        return result;
    }
}

const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
// console.log(summerCamp.registerParticipant("Petar Petarson", "student", 200));
// console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
// console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
// console.log(summerCamp.registerParticipant("Leila Wolfe", "childd", 200));

// console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
// console.log(summerCamp.unregisterParticipant("Petar"));
// console.log(summerCamp.unregisterParticipant("Petar Petarson"));


// console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
// console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
// console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
// console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
// console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));


console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp.toString());


