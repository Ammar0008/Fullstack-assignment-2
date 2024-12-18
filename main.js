function chatApp() {
    return {
        userInput: '',
        messages: [
            { sender: 'bot', text: 'Hello! How can I help you today?' }
        ],
        sendMessage() {
            if (this.userInput.trim() === '') return;

            // Add user message
            this.messages.push({ sender: 'user', text: this.userInput });

            // Mock bot reply
            this.botReply(this.userInput);

            // Clear input
            this.userInput = '';
        },
        botReply(input) {
            let reply = "Sorry, I didn't understand that.";

            // Simple keyword-based bot responses
            if (input.toLowerCase().includes('products')) {
                reply = 'We have various products like electronics, books, and textiles. What would you like to explore?';
            } else if (input.toLowerCase().includes('electronics')) {
                reply = 'Here are some popular electronics: Smartphones, Laptops, and Headphones.';
            } else if (input.toLowerCase().includes('books')) {
                reply = 'We have books across genres: Fiction, Non-Fiction, and Educational.';
            }

            // Simulate delay and add bot message
            setTimeout(() => {
                this.messages.push({ sender: 'bot', text: reply });
            }, 500);
        }
    };
}
