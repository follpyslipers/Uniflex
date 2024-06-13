const Orders = [
    {
        productName: 'JavaScript Tutorial',
        productNumber: '85743',
        paymentStatus: 'Due',
        status: 'Pending'
    },
    {
        productName: 'CSS Full Course',
        productNumber: '97245',
        paymentStatus: 'Refunded',
        status: 'Declined'
    },
    {
        productName: 'Flex-Box Tutorial',
        productNumber: '36452',
        paymentStatus: 'Paid',
        status: 'Active'
    },
]

document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.querySelector('.search-button');
    const searchBox = document.querySelector('.searchbox');
    const searchResults = document.getElementById('search-results');

    searchButton.addEventListener('click', () => {
        const searchTerm = searchBox.value.trim();
        if (searchTerm !== '') {
            fetch(`https://api.example.com/search?query=${searchTerm}`)
                .then(response => response.json())
                .then(data => {
                    displaySearchResults(data);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        } else {
            searchResults.innerHTML = 'Please enter a search term.';
        }
    });

    function displaySearchResults(results) {
        searchResults.innerHTML = ''; // Clear previous results
        if (results.length === 0) {
            searchResults.innerHTML = 'No results found.';
        } else {
            const resultList = document.createElement('ul');
            resultList.classList.add('search-results-list');
            results.forEach(result => {
                const listItem = document.createElement('li');
                listItem.textContent = result.title;
                resultList.appendChild(listItem);
            });
            searchResults.appendChild(resultList);
        }
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const userContainer = document.getElementById('user-container');
    const userList = userContainer.querySelector('.user-list');
    const loadMoreButton = userContainer.querySelector('#load-more');
    const usersPerPage = 4; // Change this value as needed
    let currentPage = 1;

    // Function to show users based on the current page
    function showUsers(page) {
        const users = userList.querySelectorAll('.user');

        users.forEach((user, index) => {
            const start = (page - 1) * usersPerPage;
            const end = start + usersPerPage;

            if (index >= start && index < end) {
                user.style.display = 'block';
            } else {
                user.style.display = 'none';
            }
        });

        if (end >= users.length) {
            loadMoreButton.style.display = 'none'; // Hide the button when all users are shown
        } else {
            loadMoreButton.style.display = 'block';
        }
    }

    showUsers(currentPage); // Show initial set of users

    loadMoreButton.addEventListener('click', () => {
        currentPage++; // Move to the next page
        showUsers(currentPage); // Show users for the next page
    });
});
