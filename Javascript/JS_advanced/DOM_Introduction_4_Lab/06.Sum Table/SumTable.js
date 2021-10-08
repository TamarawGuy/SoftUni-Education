function sumTable() {
    let sum = 0;
    const rows = document.querySelectorAll('table tr');
    for (let i = 1; i < rows.length - 1; i++) {
        let num = Number(rows[i].lastElementChild.textContent);
        sum += num;
    }
    document.getElementById('sum').textContent = sum;
}