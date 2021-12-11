function addItem() {
    const newLi = document.createElement('li');
    newLi.textContent = document.getElementById('newItemText').value;
    document.getElementById('items').appendChild(newLi);
    const button = document.createElement('a');
    button.textContent = '[Delete]';
    button.addEventListener('click', removeElement);
    button.href = '#';
    newLi.appendChild(button);
    document.getElementById('newItemText').value = '';

    function removeElement(event) {
        event.target.parentNode.remove();
    }
}