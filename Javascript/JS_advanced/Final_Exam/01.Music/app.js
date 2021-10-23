window.addEventListener('load', solve);

function solve() {
    const savedHits = document.querySelector('.saved-container')
    const likes = document.querySelector('.likes p');
    const mainDiv = document.querySelector('.all-hits-container');
    const genreInput = document.getElementById('genre');
    const nameInput = document.getElementById('name');
    const authorInput = document.getElementById('author');
    const dateInput = document.getElementById('date');

    const addBtn = document.getElementById('add-btn');

    addBtn.addEventListener('click', add);

    function add(e) {
        e.preventDefault();
        const genre = genreInput.value;
        const name = nameInput.value;
        const author = authorInput.value;
        const date = dateInput.value;

        if (genre === '' || name === '' || author === '' || date === '') {
            return
        }

        const addDiv = document.createElement('div');
        addDiv.classList.add('hits-info');

        const img = document.createElement('img');
        img.src = './static/img/img.png';
        const h2Genre = document.createElement('h2');
        h2Genre.textContent = `Genre: ${genre}`;
        const h2Name = document.createElement('h2');
        h2Name.textContent = `Name: ${name}`;
        const h2Author = document.createElement('h2');
        h2Author.textContent = `Author: ${author}`;
        const h3Date = document.createElement('h3');
        h3Date.textContent = `Date: ${date}`;
        const btnSave = document.createElement('button');
        btnSave.classList.add('save-btn');
        btnSave.textContent = 'Save song';
        const btnLike = document.createElement('button');
        btnLike.classList.add('like-btn');
        btnLike.textContent = 'Like song';
        const btnDelete = document.createElement('button');
        btnDelete.classList.add('delete-btn');
        btnDelete.textContent = 'Delete';

        addDiv.appendChild(img);
        addDiv.appendChild(h2Genre);
        addDiv.appendChild(h2Name);
        addDiv.appendChild(h2Author);
        addDiv.appendChild(h3Date);
        addDiv.appendChild(btnSave);
        addDiv.appendChild(btnLike);
        addDiv.appendChild(btnDelete);

        mainDiv.appendChild(addDiv);

        genreInput.value = '';
        nameInput.value = '';
        authorInput.value = '';
        dateInput.value = '';

        btnLike.addEventListener('click', like);

        function like(e) {
            likesNum = Number(likes.textContent.slice(-1));
            likesNum++;
            likes.textContent = `Total Likes: ${likesNum}`;

            btnLike.disabled = true;
        }

        btnSave.addEventListener('click', save);
        btnDelete.addEventListener('click', remove);

        function remove(e) {
            if (e.target.parentNode.parentNode.classList[0] === 'all-hits-container') {
                mainDiv.removeChild(addDiv);
            }
            else {
                savedHits.removeChild(addDiv);
            }
        }

        function save(e) {
            addDiv.removeChild(btnSave);
            addDiv.removeChild(btnLike);
            savedHits.appendChild(addDiv);
        }
    }
}