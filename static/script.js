fetch('/get_data')
.then(response => response.json())
.then(data => {
    data.forEach(coin => {
        // Determine the correct container based on the coin's category
        let containerId = '';
        switch (coin.category.toLowerCase()) {
            case 'enterprise':
                containerId = 'Enterprise-container';
                break;
            case 'ai':
                containerId = 'ai-tokens-container';
                break;
            case 'gaming':
                containerId = 'gaming-tokens-container';
                break;
            default:
                containerId = 'other-container'; // Ensure this container exists
        }

        const container = document.getElementById(containerId);
        const div = document.createElement('div');
        div.className = 'crypto-container';
        div.innerHTML = `<p>${coin.name} (${coin.symbol}) $ ${coin.price}</p>`;
        if (container) {
            container.appendChild(div);
        }
    });
})
.catch(error => console.error('Error:', error));
