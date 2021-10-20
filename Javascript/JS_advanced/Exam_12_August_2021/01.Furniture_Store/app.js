window.addEventListener('load', solve);

function solve() {
    let result = 0;
    const modelInput = document.querySelectorAll('input')[0];
    const yearInput = document.querySelectorAll('input')[1];
    const descriptionTextarea = document.querySelector('textarea');
    const priceInput = document.querySelectorAll('input')[2];
    const tableBody = document.querySelector('tbody');

    const addBtn = document.querySelector('#add');

    addBtn.addEventListener('click', addFurniture);

    function addFurniture(event) {
        event.preventDefault();

        const model = modelInput.value;
        const year = Number(yearInput.value);
        const description = descriptionTextarea.value;
        const price = Number(priceInput.value);


        if (model == '' || year == '' || description == '' || price == '') {
            return
        }
        else if (year < 0 || price < 0) {
            return
        }

        // Creating furniture rows and cols

        const tr1 = document.createElement('tr');
        tr1.classList.add('info');
        tr1.innerHTML += `<td>${model}</td>`;
        tr1.innerHTML += `<td>${price.toFixed(2)}</td>`;
        const td1 = document.createElement('td');
        const btnMoreInfo = document.createElement('button');
        btnMoreInfo.classList.add('moreBtn');
        btnMoreInfo.textContent = 'More Info';
        const btnBuy = document.createElement('button');
        btnBuy.classList.add('buyBtn');
        btnBuy.textContent = 'Buy it';
        td1.appendChild(btnMoreInfo);
        td1.appendChild(btnBuy);
        tr1.appendChild(td1);

        const tr2 = document.createElement('tr');
        tr2.classList.add('hide');
        tr2.innerHTML = `<td>Year: ${year}</td>`;
        const td2 = document.createElement('td');
        td2.setAttribute('colspan', 3);
        td2.textContent = `Description: ${description}`;
        tr2.appendChild(td2);

        tableBody.appendChild(tr1);
        tableBody.appendChild(tr2);

        modelInput.value = '';
        yearInput.value = '';
        descriptionTextarea.value = '';
        priceInput.value = '';

        btnMoreInfo.addEventListener('click', addInfo);

        function addInfo() {
            if (btnMoreInfo.textContent == 'More Info') {
                btnMoreInfo.textContent = 'Less Info'
                tr2.style.display = 'contents';
            }
            else {
                btnMoreInfo.textContent = 'More Info'
                tr2.style.display = 'none';
            }
        }

        btnBuy.addEventListener('click', buy);

        function buy(event) {
            const tr = event.target.parentNode.parentNode;
            const price = Number(document.querySelectorAll('.info td')[1].textContent);
            result += price;
            document.querySelector('.total-price').textContent = `${result.toFixed(2)}`;
            tr.remove();
        }
    }
}