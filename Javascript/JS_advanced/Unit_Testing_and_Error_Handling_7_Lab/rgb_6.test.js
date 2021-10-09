const { expect } = require('chai');
const { rgbToHexColor } = require('./rgb_6');


describe('RGB converter', () => {
    describe('Happy path', () => {
        it('converts white', () => {
            expect(rgbToHexColor(255, 255, 255)).to.equal('#FFFFFF');
        });

        it('converts black', () => {
            expect(rgbToHexColor(0, 0, 0)).to.equal('#000000');
        });

        it('converts SoftUni dark blue to #234465', () => {
            expect(rgbToHexColor(35, 68, 101)).to.equal('#234465');
        });
    })

    describe('Invalid parameters', () => {
        it('return undefined for missing param', () => {
            expect(rgbToHexColor(255, 255)).to.be.undefined;
        });

        it('return undefined for values out of range', () => {
            expect(rgbToHexColor(-1, -1, -1)).to.be.undefined;
        });

        it('return undefined for values out of range', () => {
            expect(rgbToHexColor(256, 256, 256)).to.be.undefined;
        });

        it('return undefined for invalid parameter type', () => {
            expect(rgbToHexColor('0', '0', '0')).to.be.undefined;
        });
    });
});