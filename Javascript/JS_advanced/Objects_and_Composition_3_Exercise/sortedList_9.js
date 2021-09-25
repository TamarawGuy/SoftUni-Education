function createSortedList() {
    let isValid = (l, index) => index >= 0 & index < l.length;

    return {
        list: [],
        size: 0,
        add(num) {
            this.list.push(num);
            this.list.sort((a, b) => a - b);
            this.size = this.list.length;
        },
        remove(index) {
            if (isValid) {
                this.list.splice(index, 1);
            }
            this.size = this.list.size;
            this.list.sort((a, b) => a - b);
        },
        get(index) {
            if (isValid) {
                return this.list[index];
            }
            this.list.sort((a, b) => a - b);
        }
    };
}