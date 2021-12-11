function previousDay(year, month, day) {
    let today = new Date(year, month - 1, day);
    today.setDate(today.getDate() - 1);
    console.log(`${today.getFullYear()}-${today.getMonth() + 1}-${today.getDate()}`);
}