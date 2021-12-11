function addItem() {
    const btn = document.querySelector('input[type="button"]').addEventListener('click', onClick);
    let text = document.getElementById('newItemText').value;
    let value = document.getElementById('newItemValue').value;

    function onClick(e) {
        let option = document.createElement('option');
        option.textContent = text;
        option.value = value;

        document.getElementById('menu').appendChild(option);
    }
    document.getElementById('newItemText').value = '';
    document.getElementById('newItemValue').value = '';
}