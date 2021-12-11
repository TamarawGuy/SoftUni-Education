const { isOddOrEven } = require('./evenOrOdd_2');
const { expect } = require('chai');

describe('Odd or even length', () => {
    it('return even length', () => {
        expect(isOddOrEven('even')).to.equal('even');
    });

    it('return odd', () => {
        expect(isOddOrEven('odd')).to.equal('odd');
    });

    it('return undefined', () => {
        expect(isOddOrEven(5)).to.be.undefined;
    });
})