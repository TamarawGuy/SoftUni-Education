function solve() {

    fighter = (name) => {
        return {
            name,
            health: 100,
            stamina: 100,
            fight() {
                this.stamina -= 1;
                console.log(`${this.name} slashes at the foe!`);
            }
        }
    },
        mage = (name) => {
            return {
                name,
                health: 100,
                mana: 100,
                cast(spell) {
                    this.mana -= 1;
                    console.log(`${this.name} cast ${spell}`);
                }
            }
        }
    return { mage: mage, fighter: fighter };
}