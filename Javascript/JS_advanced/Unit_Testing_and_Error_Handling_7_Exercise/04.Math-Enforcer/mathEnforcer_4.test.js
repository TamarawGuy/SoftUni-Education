const { mathEnforcer } = require('./mathEnforcer_4');
const { expect } = require('chai');

describe('test mathEnforcer', () => {
    describe('test addFive method with wrong input and expect undefined', () => {
        it('expect undefined on string input type', () => {
            expect(mathEnforcer.addFive('5')).to.be.undefined;
        });

        it('expect undefined on array input type', () => {
            expect(mathEnforcer.addFive([])).to.be.undefined;
        });

        it('expect undefined on object input type', () => {
            expect(mathEnforcer.addFive({})).to.be.undefined;
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.addFive(undefined)).to.be.undefined;
        });
    });

    describe('test addFive method with proper input expect success', () => {
        it('expect proper number outcome', () => {
            expect(mathEnforcer.addFive(3)).to.equal(8);
        });

        it('expect proper number outcome', () => {
            expect(mathEnforcer.addFive(-3)).to.equal(2);
        });

        it('expect proper number outcome', () => {
            expect(mathEnforcer.addFive(-3.3)).to.be.closeTo(1.7, 0.01);
        });
    });

    describe('test subtractTen method with wrong input type expect undefined', () => {
        it('expect undefined on string input type', () => {
            expect(mathEnforcer.subtractTen('5')).to.be.undefined;
        });

        it('expect undefined on array input type', () => {
            expect(mathEnforcer.subtractTen([])).to.be.undefined;
        });

        it('expect undefined on object input type', () => {
            expect(mathEnforcer.subtractTen({})).to.be.undefined;
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.subtractTen(undefined)).to.be.undefined;
        });
    });

    describe('test subtractTen method with proper input type expect success', () => {
        it('expect proper number outcome', () => {
            expect(mathEnforcer.subtractTen(5)).to.equal(-5);
        });

        it('expect proper number outcome', () => {
            expect(mathEnforcer.subtractTen(-3)).to.equal(-13);
        });

        it('expect proper number outcome', () => {
            expect(mathEnforcer.subtractTen(20.2)).to.closeTo(10.2, 0.01);
        });
    });

    describe('test sum method with wrong input type', () => {
        it('expect undefined on first parameter as string', () => {
            expect(mathEnforcer.sum('5', 2)).to.be.undefined;
        });

        it('expect undefined on second parameter as string', () => {
            expect(mathEnforcer.sum(5, '2')).to.be.undefined;
        });

        it('expect undefined on array input type', () => {
            expect(mathEnforcer.sum([], 2)).to.be.undefined;
        });

        it('expect undefined on array input type', () => {
            expect(mathEnforcer.sum(2, [])).to.be.undefined;
        });

        it('expect undefined on object input type', () => {
            expect(mathEnforcer.sum({}, 2)).to.be.undefined;
        });

        it('expect undefined on object input type', () => {
            expect(mathEnforcer.sum(2, {})).to.be.undefined;
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(2, undefined)).to.be.undefined;
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(undefined, 2)).to.be.undefined;
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(undefined, undefined)).to.be.undefined;
        });
    });

    describe('test sum method with proper input type', () => {
        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(2, 2)).to.equal(4);
        });

        it('expect proper number outcome', () => {
            expect(mathEnforcer.sum(-1, -2)).to.equal(-3);
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(2.2, 2)).to.be.closeTo(4.2, 0.01);
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(-2.2, 2)).to.be.closeTo(-0.2, 0.01);
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(2, 2.2)).to.be.closeTo(4.2, 0.01);
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(2.2, 2.2)).to.be.closeTo(4.4, 0.01);
        });

        it('expect undefined on undefined input type', () => {
            expect(mathEnforcer.sum(-2.2, -2.2)).to.be.closeTo(-4.4, 0.01);
        });
    });
});