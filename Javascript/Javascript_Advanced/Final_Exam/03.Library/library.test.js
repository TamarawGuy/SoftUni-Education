const { library } = require('./library');
const { expect } = require('chai');

describe('library', () => {
    describe('calcPriceOfBook', () => {
        it('invalid input types', () => {
            expect(() => library.calcPriceOfBook(undefined, undefined)).to.throw()
            expect(() => library.calcPriceOfBook('Name', 0.5)).to.throw();
            expect(() => library.calcPriceOfBook(1, 2001)).to.throw();
        });

        it('when year is less or equal to 1980', () => {
            expect(library.calcPriceOfBook('Name', 1979)).to.equal("Price of Name is 10.00");
            expect(library.calcPriceOfBook('Name', 1980)).to.equal("Price of Name is 10.00");
        });

        it('when year is above 1980', () => {
            expect(library.calcPriceOfBook('Name', 1981)).to.equal("Price of Name is 20.00");
            expect(library.calcPriceOfBook('Name', 3100)).to.equal("Price of Name is 20.00");
        });
    });

    describe('findBook', () => {
        it('when length of arr is 0', () => {
            expect(() => library.findBook([], 'Name')).to.throw()
        });

        it('when the desiredBook is not presented', () => {
            expect(library.findBook(['Name1', 'Name2'], 'Name')).to.equal("The book you are looking for is not here!");
        });

        it('when the desiredBook is presented', () => {
            expect(library.findBook(['Name1', 'Name2'], 'Name1')).to.equal("We found the book you want.");
        });
    });

    describe('arrangeTheBooks', () => {
        it('when countBooks is not integer', () => {
            expect(() => library.arrangeTheBooks(5.55)).to.throw();
        });

        it('when countBooks is negative', () => {
            expect(() => library.arrangeTheBooks(-1)).to.throw();
        });

        it('when there is not enough space for the books', () => {
            expect(library.arrangeTheBooks(41)).to.equal('Insufficient space, more shelves need to be purchased.');
        });

        it('when there is enough space for the books', () => {
            expect(library.arrangeTheBooks(39)).to.equal('Great job, the books are arranged.');
            expect(library.arrangeTheBooks(40)).to.equal('Great job, the books are arranged.');
        });
    });
});