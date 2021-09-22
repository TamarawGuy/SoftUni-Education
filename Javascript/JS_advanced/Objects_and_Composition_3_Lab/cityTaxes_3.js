function cityRecordContinue(name, population, treasury) {
    const city = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += population * this.taxRate;
        },
        applyGrowth(percent) {
            this.population += Math.floor(percent / 100 * this.population);
        },
        applyRecession(percent) {
            this.treasury -= Math.ceil(this.treasury * percent / 100);
        },
    };
    return city;
}