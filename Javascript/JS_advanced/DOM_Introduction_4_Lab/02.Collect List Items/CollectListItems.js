function extractText() {
    let result = '';
    document.querySelectorAll('#items li').forEach(el => {
        result += el.textContent + '\n';
    })

    document.querySelector('#result').textContent = result;
}