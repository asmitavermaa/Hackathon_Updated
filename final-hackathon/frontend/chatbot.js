document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chatbox");
    const userMessageInput = document.getElementById("user-message");
    const sendButton = document.getElementById("send-button");

    function appendUserMessage(message) {
        chatBox.innerHTML += `<div class="message user-message">You: ${message}</div>`;
    }

    function appendBotMessage(message) {
        chatBox.innerHTML += `<div class="message bot-message">Chatbot: ${message}</div>`;
    }

    // Function to send a message to the chatbot
    function sendMessage() {
        const userInput = userMessageInput.value.trim();
        if (userInput === "") {
            return;
        }

        appendUserMessage(userInput);
        const chatbotApiEndpoint = 'http://localhost:8080/chatbot'; 
        fetch(chatbotApiEndpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userInput }),
        })
        .then(response => response.json())
        .then(data => {
            const chatbotResponse = data.content;
            appendBotMessage(chatbotResponse);
        })
        .catch(error => {
            console.error('Error:', error);
        });

        userMessageInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    userMessageInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    sendButton.addEventListener("click", sendMessage);
});
