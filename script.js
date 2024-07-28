const chatLog = document.getElementById('chat-log');
const referenceLog = document.getElementById('reference-log');
const askQuestionForm = document.getElementById('ask-question-form');
const questionInput = document.getElementById('question-input');

askQuestionForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();
    if (question !== '') {
        // Send request to server to get answer
        fetch('/get-answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question }),
        })
            .then((response) => response.json())
            .then((data) => {
                const answer = data.answer;
                const rating = data.rating;
                const logItem = document.createElement('li');
                logItem.textContent = `${question}: ${answer} (${rating}/5)`;
                chatLog.appendChild(logItem);
            })
            .catch((error) => console.error(error));
    }
});

// Update reference log
fetch('/get-reference-log')
    .then((response) => response.json())
    .then((data) => {
        const referenceItems = data.referenceItems;
        referenceItems.forEach((item) => {
            const logItem = document.createElement('li');
            logItem.textContent = item;
            referenceLog.appendChild(logItem);
        });
    })
    .catch((error) => console.error(error));
