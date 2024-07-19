class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value;
        
    
        if (text1.length > 500) {
            this.displayAlert(chatbox, "Maximum character limit exceeded (500 characters)");
            return;
        }

        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 };
        this.messages.push(msg1);
        this.updateChatText(chatbox);

     
        let typingIndicator = { name: "Jigyasa", message: "", isTyping: true };
        this.messages.push(typingIndicator);
        this.updateChatText(chatbox);

      
        this.translateText(text1).then(data => {
    
            this.messages = this.messages.filter(msg => !msg.isTyping);
            
    
            let responseMessage = `
                 ${data.response}
                <br>Source: <a href="${data.url}" target="_blank">${data.url}</a>
            `;
            let msg2 = { name: "Jigyasa", message: responseMessage };
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            textField.value = '';
        }).catch(error => {
            console.error('Translation Error:', error);
            this.messages = this.messages.filter(msg => !msg.isTyping);
            let errorMessage = { name: "Jigyasa", message: "There was an error processing your request. Please try again." };
            this.messages.push(errorMessage);
            this.updateChatText(chatbox);
            textField.value = '';
        });
    }

    displayAlert(chatbox, message) {
        let alertMessage = { name: "Alert", message: message };
        this.messages.push(alertMessage);
        this.updateChatText(chatbox);
    }

    translateText(text) {
        const url = `http://localhost:3002/proxy/jigyasa`; 
        const requestBody = {
            input: text
        };

        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                return data.data;  
            } else {
                throw new Error('Translation API Error');
            }
        })
        .catch(error => {
            console.error('Translation API Error:', error);
            throw error;
        });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.isTyping) {
                html += '<div class="messages__item messages__item--typing"></div>';
            } else if (item.name === "Jigyasa") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();
