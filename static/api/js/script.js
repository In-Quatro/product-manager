// Функция для отображения уведомлений
const showNotification = (message, color = '#caa349') => {
    const notification = document.getElementById('notification');
    notification.innerText = message;
    notification.style.display = 'block';
    notification.style.background = color;
    setTimeout(() => {
        notification.style.display = 'none';
    }, 5000);
};

// Отображение товара из БД
const fetchProducts = () => {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('productTable').querySelector('tbody');
            tbody.innerHTML = '';
            data.forEach(product => {
                const row = `<tr>
                            <td>${product.name}</td>
                            <td>${product.description}</td>
                            <td>${product.price}</td>
                        </tr>`;
                tbody.innerHTML += row;
            });
        });
};

document.getElementById('productForm').addEventListener('submit', function
    (event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = parseFloat(document.getElementById('price').value);

    // Проверки на стороне клиента
    if (name.trim() === '') {
        showNotification('Название не может быть пустым.', 'red');
        return;
    }
    if (description.trim() === '') {
        showNotification('Описание не может быть пустым.', 'red');
        return;
    }
    if (description.length > 100) {
        showNotification('Описание не должно превышать 100 символов.', 'red');
        return;
    }
    if (price <= 0) {
        showNotification('Цена должна быть положительным числом.', 'red');
        return;
    }

    const productData = {
        name: name,
        description: description,
        price: price
    };

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(productData)
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(err.detail || 'Ошибка сети');
                });
            }
            return response.json();
        })
        .then(data => {
            showNotification('Продукт успешно добавлен');
            document.getElementById('productForm').reset();
            fetchProducts();
        })
        .catch((error) => {
            console.error('Ошибка:', error);
            showNotification('Произошла ошибка при добавлении продукта: ' + error.message, 'red');
        });
});

// Загрузка продуктов при загрузке страницы
window.onload = fetchProducts;