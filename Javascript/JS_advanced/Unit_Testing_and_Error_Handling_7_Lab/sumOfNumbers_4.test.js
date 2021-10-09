const { sum } = require('./sumOfNumbers_4');
const { expect } = require('chai');

describe('Sum of array', () => {
    it('take array as param', () => {
        expect(sum([1, 2, 3])).to.equal(6);
    });
})