# app.py

import os
from flask import Flask, render_template, request
from response_agent import ResponseAgent  # Import the ResponseAgent class from your chatbot module

app = Flask(__name__)

response_agent = ResponseAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = response_agent.respond(user_input)
        response_agent.chat_history.append({'user_input': user_input, 'response': response})
        return render_template('index.html', chat_history=response_agent.chat_history)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
