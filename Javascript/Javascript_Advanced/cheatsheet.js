// Selecting DOM elements
const element = document.getElementById('content');
document.querySelector('#content');
document.querySelectorAll('ul li');

// Get/Set content
element.textContent;
element.value;

// Traversing DOM
element.parentElement;
element.children;

// Create element
const p = document.createElement('p');

// Adding to DOM
element.appendChild(para);

// Events
element.addEventListener('click', e => {
    console.log(e.target);
})