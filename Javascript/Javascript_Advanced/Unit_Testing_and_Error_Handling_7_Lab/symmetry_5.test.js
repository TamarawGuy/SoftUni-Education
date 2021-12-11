const { expect, assert } = require('chai');
const { isSymmetric } = require('./symmetry_5');

describe('symmetry checker', () => {
    it('return true for symmetic array', () => {
        expect(isSymmetric([1, 2, 2, 1])).to.be.true;
    });

    it('return false for non-symmetric array', () => {
        expect(isSymmetric([1, 2, 3, 4])).to.be.false;
    });

    it('return false for non-array type', () => {
        expect(isSymmetric('string')).to.be.false;
    });

    it('return true for symmetic array with odd length', () => {
        expect(isSymmetric([1, 2, 1])).to.be.true;
    });

    it('return true for symmetic array with string elements', () => {
        expect(isSymmetric(['1', '2', '2', '1'])).to.be.true;
    });

    it('return false for non-symmetic array with string elements', () => {
        expect(isSymmetric(['a', 'b', 'c'])).to.be.false;
    });

    it('return false for symmetric string', () => {
        expect(isSymmetric('abba')).to.be.false;
    });

    it('return true for type-different array', () => {
        expect(isSymmetric([1, 2, 2, '1'])).to.be.false;
    });
})
