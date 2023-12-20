const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value.trim();
    
    if (userMessage !== '') {
        displayMessage('User', userMessage);
        
        // Replace with your actual API endpoint and logic
        fetch('YOUR_API_ENDPOINT', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const responseMessage = data.answer; // Assuming API response structure
            displayMessage('AIMY', responseMessage);
        })
        .catch(error => {
            console.error('Error:', error);
            displayMessage('AIMY', 'An error occurred while fetching the answer.');
        });
        
        userInput.value = '';
    }
});

function displayMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender.toLowerCase());
    messageElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
