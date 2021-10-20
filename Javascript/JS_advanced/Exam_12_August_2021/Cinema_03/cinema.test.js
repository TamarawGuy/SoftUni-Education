const { cinema } = require('./cinema');
const { expect } = require('chai');


describe('Tests cinema', () => {
    describe('test showMovies', () => {
        it('test with array with 0 length', () => {
            expect(cinema.showMovies([])).to.equal('There are currently no movies to show.');
        });

        it('test with valid input array', () => {
            expect(cinema.showMovies(['m1, m2, m3'])).to.equal('m1, m2, m3');
            expect(cinema.showMovies([1, 2, 3])).to.equal('1, 2, 3');
        });
    });

    describe('test ticketPrice', () => {
        it('test with invalid property', () => {
            expect(() => cinema.ticketPrice('Invalid')).to.throw();
            expect(() => cinema.ticketPrice(12)).to.throw();
            expect(() => cinema.ticketPrice()).to.throw();
        });

        it('test with valid input', () => {
            expect(cinema.ticketPrice('Premiere')).to.equal(12);
            expect(cinema.ticketPrice('Normal')).to.equal(7.5);
            expect(cinema.ticketPrice('Discount')).to.equal(5.5);
        });
    });

    describe('test swapSeatsInHall', () => {
        it('test with invalid input data', () => {
            expect(cinema.swapSeatsInHall(50, 21)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 21)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall('1', '2')).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall()).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(0, 0)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(-1, -1)).to.equal('Unsuccessful change of seats in the hall.');
        });

        it('test with valid input data', () => {
            expect(cinema.swapSeatsInHall(1, 10)).to.equal('Successful change of seats in the hall.');
        });
    });
});