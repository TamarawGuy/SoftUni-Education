class Stringer {
    constructor(innerString, innerLength) {
        this.innerString = innerString;
        this.innerLength = innerLength;
        this.threeDots = '...';
    }

    increase(length) {
        if (length + this.innerLength <= 0) {
            this.innerLength = 0;
        }
        else {
            this.innerLength += length;
        }

    }

    decrease(length) {
        if (this.innerLength - length < 0) {
            this.innerLength = 0;
        }
        else {
            this.innerLength -= length;
        }
    }

    toString() {
        if (this.innerLength === 0) {
            return this.threeDots;
        }
        else if (this.innerString.length > this.innerLength) {
            return this.innerString.slice(0, this.innerString.length - this.innerLength) + this.threeDots;
        }
        else {
            return this.innerString;
        }
    }
}

let test = new Stringer("Test", 5);
console.log(test.toString()); // Test
test.decrease(3);
console.log(test.toString()); // Te...
test.decrease(5);
console.log(test.toString()); // ...
test.increase(4);
console.log(test.toString());