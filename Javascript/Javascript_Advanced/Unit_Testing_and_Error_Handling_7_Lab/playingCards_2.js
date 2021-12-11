function createCard(face, suit) {
    const faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    const suits = {
        'S': '\u2660',
        'H': '\u2665',
        'D': '\u2666',
        'C': '\u2663'
    }

    if (faces.includes(face) == false) {
        throw new Error("Invalid face!")
    }

    if (Object.keys(suits).includes(suit) == false) {
        throw new Error("Invalid suit!")
    }

    return {
        face,
        suit: suits[suit],
        toString() {
            return this.face + this.suit;
        }
    }
}


let card1 = createCard('A', 'S');
console.log(card1.toString());
let card2 = createCard('10', 'H');
console.log(card2.toString());
let card3 = createCard('1', 'C');
console.log(card3.toString());

let card4 = createCard('9', 'Y');
console.log(card4.toString());
